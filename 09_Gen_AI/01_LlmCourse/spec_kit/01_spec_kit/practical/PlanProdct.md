# Technical Implementation Plan
## WooCommerce AI Product Generator Plugin

**Project**: WooCommerce AI Product Generator  
**Version**: 1.0.0  
**Plan Date**: April 9, 2026  
**AI Agent**: Claude  
**Target Platform**: WordPress 6.0+ / WooCommerce 7.0+

---

## 1. Executive Summary

This plan outlines the technical architecture and implementation strategy for a WooCommerce plugin that leverages AI to automatically generate product titles and descriptions. The plugin will support multiple AI providers (OpenAI, Anthropic Claude, Google Gemini), feature both single and bulk generation capabilities, and provide an intuitive React-based admin interface.

### Key Objectives
- Enable one-click AI generation of product titles and descriptions
- Support multiple AI providers with a unified interface
- Provide bulk processing for large product catalogs
- Maintain WordPress and WooCommerce coding standards
- Ensure security, performance, and scalability

---

## 2. Technical Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    WordPress Admin UI                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Settings   │  │   Single     │  │     Bulk     │      │
│  │     Page     │  │  Generation  │  │  Generation  │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                  │               │
│         └─────────────────┴──────────────────┘               │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           WordPress REST API Layer                   │   │
│  │  /wp-json/waipg/v1/generate                         │   │
│  │  /wp-json/waipg/v1/bulk-process                     │   │
│  │  /wp-json/waipg/v1/templates                        │   │
│  └──────────────────────┬──────────────────────────────┘   │
└─────────────────────────┼────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Core Plugin Logic                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Product    │  │   Template   │  │     Bulk     │      │
│  │  Generator   │  │    Manager   │  │  Processor   │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                  │               │
│         └─────────────────┴──────────────────┘               │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         AI Provider Factory & Interface              │   │
│  └──────────────────────┬──────────────────────────────┘   │
└─────────────────────────┼────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  OpenAI  │    │  Claude  │    │  Gemini  │
    │ Provider │    │ Provider │    │ Provider │
    └──────────┘    └──────────┘    └──────────┘
          │               │               │
          └───────────────┴───────────────┘
                          │
                          ▼
                  External AI APIs
```

### 2.2 Component Breakdown

#### 2.2.1 Plugin Core Structure

```
woocommerce-ai-product-generator/
├── woocommerce-ai-product-generator.php  # Main plugin file
├── uninstall.php                         # Cleanup on uninstall
├── readme.txt                            # WordPress.org readme
├── composer.json                         # PHP dependencies
├── package.json                          # Node dependencies
├── webpack.config.js                     # Build configuration
│
├── includes/                             # Core PHP classes
│   ├── class-waipg-plugin.php           # Main plugin class
│   ├── class-waipg-activator.php        # Activation hooks
│   ├── class-waipg-deactivator.php      # Deactivation hooks
│   ├── class-waipg-loader.php           # Hooks loader
│   │
│   ├── providers/                        # AI Provider implementations
│   │   ├── interface-waipg-ai-provider.php
│   │   ├── class-waipg-openai-provider.php
│   │   ├── class-waipg-claude-provider.php
│   │   ├── class-waipg-gemini-provider.php
│   │   └── class-waipg-provider-factory.php
│   │
│   ├── generators/                       # Generation logic
│   │   ├── class-waipg-product-generator.php
│   │   ├── class-waipg-template-manager.php
│   │   └── class-waipg-response-handler.php
│   │
│   ├── processors/                       # Bulk processing
│   │   ├── class-waipg-bulk-processor.php
│   │   ├── class-waipg-queue-manager.php
│   │   └── class-waipg-progress-tracker.php
│   │
│   └── utils/                            # Utility classes
│       ├── class-waipg-encryption.php
│       ├── class-waipg-logger.php
│       └── class-waipg-validator.php
│
├── admin/                                # Admin-specific functionality
│   ├── class-waipg-admin.php            # Admin hooks and pages
│   ├── class-waipg-settings.php         # Settings management
│   ├── class-waipg-meta-box.php         # Product edit meta box
│   │
│   ├── js/                               # JavaScript source
│   │   ├── src/
│   │   │   ├── index.js
│   │   │   ├── components/
│   │   │   │   ├── SettingsPage.jsx
│   │   │   │   ├── GeneratorPanel.jsx
│   │   │   │   ├── BulkGenerator.jsx
│   │   │   │   ├── TemplateEditor.jsx
│   │   │   │   └── PreviewModal.jsx
│   │   │   ├── hooks/
│   │   │   └── utils/
│   │   └── build/                        # Compiled JS (gitignored)
│   │
│   ├── css/                              # Stylesheets
│   │   ├── src/
│   │   │   └── admin.scss
│   │   └── build/                        # Compiled CSS (gitignored)
│   │
│   └── partials/                         # PHP template partials
│       ├── settings-page.php
│       └── meta-box.php
│
├── api/                                  # REST API endpoints
│   ├── class-waipg-rest-api.php         # REST controller
│   └── class-waipg-rest-validator.php   # Request validation
│
├── templates/                            # Prompt templates
│   ├── default-title.json
│   ├── default-description.json
│   └── schema.json
│
├── languages/                            # Translations
│   └── woocommerce-ai-product-generator.pot
│
└── tests/                                # Test suites
    ├── phpunit.xml
    ├── bootstrap.php
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## 3. Core Components Specification

### 3.1 AI Provider Interface

**File**: `includes/providers/interface-waipg-ai-provider.php`

```php
<?php
/**
 * AI Provider Interface
 * 
 * Defines the contract all AI providers must implement
 */
interface WAIPG_AI_Provider {
    
    /**
     * Generate content based on prompt
     * 
     * @param string $prompt The generation prompt
     * @param array  $options Provider-specific options
     * @return array {
     *     @type bool   $success   Whether generation succeeded
     *     @type string $content   Generated content
     *     @type string $error     Error message if failed
     *     @type int    $tokens    Tokens used (if available)
     * }
     */
    public function generate( string $prompt, array $options = [] ): array;
    
    /**
     * Validate API credentials
     * 
     * @return array {
     *     @type bool   $valid   Whether credentials are valid
     *     @type string $message Status message
     * }
     */
    public function validate_credentials(): array;
    
    /**
     * Get provider name
     * 
     * @return string Provider identifier
     */
    public function get_name(): string;
    
    /**
     * Get provider display name
     * 
     * @return string Provider display name
     */
    public function get_display_name(): string;
    
    /**
     * Get default model
     * 
     * @return string Default model identifier
     */
    public function get_default_model(): string;
    
    /**
     * Get available models
     * 
     * @return array List of available models
     */
    public function get_available_models(): array;
    
    /**
     * Set API key
     * 
     * @param string $api_key The API key
     */
    public function set_api_key( string $api_key ): void;
    
    /**
     * Set model
     * 
     * @param string $model Model identifier
     */
    public function set_model( string $model ): void;
}
```

**Implementation Strategy**:
- Each provider class implements this interface
- Factory pattern for instantiation based on user settings
- Unified error handling across all providers
- Consistent response format for easy interoperability

### 3.2 Provider Factory

**File**: `includes/providers/class-waipg-provider-factory.php`

**Responsibilities**:
1. Instantiate the correct provider based on settings
2. Inject credentials securely
3. Cache provider instances (singleton per provider type)
4. Handle provider-specific configuration

**Key Methods**:
```php
class WAIPG_Provider_Factory {
    public static function create( string $provider_name ): WAIPG_AI_Provider;
    public static function get_available_providers(): array;
    public static function is_provider_available( string $provider_name ): bool;
}
```

### 3.3 Product Generator

**File**: `includes/generators/class-waipg-product-generator.php`

**Core Workflow**:
```
1. Extract product data (title, category, attributes, price, etc.)
2. Load applicable template
3. Populate template with product data
4. Send to AI provider
5. Validate and sanitize response
6. Return formatted result
```

**Key Methods**:
```php
class WAIPG_Product_Generator {
    /**
     * Generate product title
     * 
     * @param int   $product_id WooCommerce product ID
     * @param array $options    Generation options
     * @return array Generation result
     */
    public function generate_title( int $product_id, array $options = [] ): array;
    
    /**
     * Generate product description
     * 
     * @param int   $product_id WooCommerce product ID
     * @param array $options    Generation options
     * @return array Generation result
     */
    public function generate_description( int $product_id, array $options = [] ): array;
    
    /**
     * Generate both title and description
     * 
     * @param int   $product_id WooCommerce product ID
     * @param array $options    Generation options
     * @return array Generation results
     */
    public function generate_both( int $product_id, array $options = [] ): array;
}
```

**Product Data Extraction**:
- Product name (existing)
- Category/categories
- Tags
- Attributes (size, color, etc.)
- Price
- Stock status
- Short description (if exists)
- Custom fields
- Images (can be used for context)

### 3.4 Template Manager

**File**: `includes/generators/class-waipg-template-manager.php`

**Template Structure** (JSON):
```json
{
  "id": "default-title",
  "name": "Default Product Title",
  "type": "title",
  "prompt": "Generate a compelling product title for an e-commerce product with the following details:\n\nProduct Name: {{product_name}}\nCategory: {{category}}\nPrice: {{price}}\nKey Features: {{attributes}}\n\nRequirements:\n- Maximum 60 characters\n- Include primary keyword: {{category}}\n- SEO optimized\n- {{tone}} tone\n\nGenerate ONLY the title, no additional text.",
  "variables": [
    "product_name",
    "category",
    "price",
    "attributes",
    "tone"
  ],
  "settings": {
    "max_tokens": 100,
    "temperature": 0.7
  }
}
```

**Key Features**:
- Variable substitution: `{{variable_name}}`
- Conditional sections: `{{#if variable}}...{{/if}}`
- Custom templates per product category
- Import/export templates
- Template validation

### 3.5 Bulk Processor

**File**: `includes/processors/class-waipg-bulk-processor.php`

**Architecture**:
- Uses Action Scheduler (WooCommerce's background processing library)
- Queue-based processing to avoid timeouts
- Configurable batch sizes (default: 5 products per batch)
- Progress tracking via transients
- Email notification on completion

**Process Flow**:
```
1. User selects products to process
2. Create queue entries in Action Scheduler
3. Process in background (5 products at a time)
4. Update progress transient after each batch
5. Send notification on completion
6. Clean up completed queues
```

**Key Methods**:
```php
class WAIPG_Bulk_Processor {
    public function queue_products( array $product_ids, array $options ): string;
    public function get_progress( string $batch_id ): array;
    public function cancel_batch( string $batch_id ): bool;
    public function process_batch( array $product_ids, array $options ): array;
}
```

---

## 4. Data Layer

### 4.1 WordPress Options

**Settings Storage** (wp_options table):

```
waipg_settings = {
    'provider': 'openai',           // Selected AI provider
    'openai_api_key': 'encrypted',  // Encrypted API key
    'claude_api_key': 'encrypted',
    'gemini_api_key': 'encrypted',
    'openai_model': 'gpt-4',
    'claude_model': 'claude-sonnet-4-6',
    'gemini_model': 'gemini-2.0-flash-exp',
    'default_tone': 'professional',
    'default_length': 'medium',
    'enable_seo': true,
    'max_retries': 3,
    'timeout': 30,
    'enable_logging': true
}
```

**Encryption Strategy**:
- Use `openssl_encrypt()` with AES-256-CBC
- Encryption key derived from WordPress AUTH_KEY and SECURE_AUTH_KEY
- IV (initialization vector) stored separately
- Decrypt only when needed for API calls

### 4.2 Product Meta Fields

**Per-Product Settings** (WooCommerce product meta):

```
_waipg_auto_generate: 'yes'|'no'        // Auto-generate on product creation
_waipg_last_generated: '2026-04-09'     // Last generation timestamp
_waipg_history: [                        // Generation history
    {
        'type': 'title',
        'content': 'Generated Title',
        'provider': 'openai',
        'timestamp': '2026-04-09 10:30:00',
        'tokens': 25
    }
]
_waipg_custom_template: 'template-id'    // Custom template override
```

### 4.3 Transients (Temporary Data)

```
waipg_bulk_progress_{batch_id}: {        // Bulk processing progress
    'total': 100,
    'processed': 45,
    'successful': 42,
    'failed': 3,
    'started': '2026-04-09 10:00:00',
    'updated': '2026-04-09 10:15:00'
}
```

**TTL**: 1 hour (auto-cleanup after completion or expiry)

---

## 5. REST API Specification

### 5.1 Endpoints

**Base URL**: `/wp-json/waipg/v1`

#### 5.1.1 Generate Title

```
POST /wp-json/waipg/v1/generate/title

Request Body:
{
    "product_id": 123,
    "provider": "openai",        // Optional, uses default if not specified
    "template_id": "custom-123", // Optional
    "options": {
        "tone": "professional",
        "length": "short",
        "keywords": ["organic", "natural"]
    }
}

Response (200 OK):
{
    "success": true,
    "data": {
        "title": "Premium Organic Cotton T-Shirt - Eco-Friendly & Sustainable",
        "tokens_used": 28,
        "provider": "openai",
        "model": "gpt-4",
        "timestamp": "2026-04-09T10:30:00Z"
    }
}

Response (400 Bad Request):
{
    "success": false,
    "error": {
        "code": "invalid_product",
        "message": "Product ID 123 does not exist"
    }
}
```

#### 5.1.2 Generate Description

```
POST /wp-json/waipg/v1/generate/description

Request Body:
{
    "product_id": 123,
    "provider": "claude",
    "options": {
        "tone": "casual",
        "length": "long",
        "include_benefits": true,
        "include_specs": true
    }
}

Response (200 OK):
{
    "success": true,
    "data": {
        "description": "<p>Discover the perfect blend of comfort...</p>",
        "tokens_used": 456,
        "provider": "claude",
        "model": "claude-sonnet-4-6"
    }
}
```

#### 5.1.3 Bulk Process

```
POST /wp-json/waipg/v1/bulk/start

Request Body:
{
    "product_ids": [123, 456, 789],
    "generate_type": "both",  // 'title', 'description', 'both'
    "provider": "openai",
    "options": {
        "tone": "professional",
        "overwrite_existing": false
    }
}

Response (202 Accepted):
{
    "success": true,
    "data": {
        "batch_id": "batch_abc123",
        "total_products": 3,
        "status_url": "/wp-json/waipg/v1/bulk/status/batch_abc123"
    }
}
```

#### 5.1.4 Bulk Status

```
GET /wp-json/waipg/v1/bulk/status/{batch_id}

Response (200 OK):
{
    "success": true,
    "data": {
        "batch_id": "batch_abc123",
        "status": "processing",  // 'queued', 'processing', 'completed', 'failed'
        "total": 100,
        "processed": 45,
        "successful": 42,
        "failed": 3,
        "progress_percent": 45,
        "started_at": "2026-04-09T10:00:00Z",
        "updated_at": "2026-04-09T10:15:00Z",
        "errors": [
            {
                "product_id": 789,
                "error": "API rate limit exceeded"
            }
        ]
    }
}
```

#### 5.1.5 Templates

```
GET /wp-json/waipg/v1/templates
POST /wp-json/waipg/v1/templates
PUT /wp-json/waipg/v1/templates/{id}
DELETE /wp-json/waipg/v1/templates/{id}
```

### 5.2 Authentication & Authorization

**Authentication**:
- WordPress cookie authentication for admin interface
- Application passwords for external integrations

**Authorization**:
- Requires `manage_woocommerce` capability
- Nonce verification for all state-changing requests
- Rate limiting: 60 requests per minute per user

**Security Headers**:
```php
$allowed_methods = ['POST', 'GET', 'PUT', 'DELETE'];
permission_callback => function() {
    return current_user_can( 'manage_woocommerce' );
}
```

---

## 6. Frontend Architecture (React)

### 6.1 Technology Stack

- **React**: 18.2+
- **Build Tool**: Webpack 5
- **Transpiler**: Babel 7
- **UI Components**: @wordpress/components
- **State Management**: React Context API + hooks
- **HTTP Client**: @wordpress/api-fetch
- **Styling**: SCSS with CSS modules

### 6.2 Component Hierarchy

```
<App>
  ├── <SettingsPage>
  │   ├── <ProviderSelector>
  │   ├── <APIKeyInput>
  │   ├── <ModelSelector>
  │   └── <DefaultSettings>
  │
  ├── <GeneratorPanel> (Single Product)
  │   ├── <GenerationForm>
  │   ├── <OptionsPanel>
  │   ├── <PreviewModal>
  │   └── <HistoryList>
  │
  ├── <BulkGenerator>
  │   ├── <ProductSelector>
  │   ├── <BulkOptions>
  │   ├── <ProgressBar>
  │   └── <ResultsTable>
  │
  └── <TemplateEditor>
      ├── <TemplateList>
      ├── <TemplateForm>
      └── <VariableHelper>
```

### 6.3 State Management

**Global Context**:
```javascript
const AppContext = {
    settings: {
        provider: 'openai',
        models: {...},
        defaults: {...}
    },
    templates: [...],
    bulkProgress: {...},
    notifications: [...]
}
```

**Custom Hooks**:
```javascript
useGenerator()      // Handle generation requests
useTemplates()      // Manage templates
useBulkProcessor()  // Manage bulk operations
useSettings()       // Read/write settings
```

### 6.4 Build Configuration

**webpack.config.js**:
```javascript
module.exports = {
    entry: './admin/js/src/index.js',
    output: {
        path: path.resolve(__dirname, 'admin/js/build'),
        filename: 'admin.js'
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                use: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }
        ]
    },
    externals: {
        react: 'React',
        'react-dom': 'ReactDOM',
        '@wordpress/api-fetch': 'wp.apiFetch',
        '@wordpress/components': 'wp.components',
        '@wordpress/i18n': 'wp.i18n'
    }
}
```

**Benefits**:
- Reduces bundle size by using WordPress's built-in React
- Leverages WordPress UI components for consistency
- Automatic i18n support

---

## 7. Security Implementation

### 7.1 Input Validation

**All API Endpoints**:
```php
// Product ID validation
$product_id = absint( $request->get_param( 'product_id' ) );
if ( ! wc_get_product( $product_id ) ) {
    return new WP_Error( 'invalid_product', __( 'Invalid product ID', 'waipg' ) );
}

// Provider validation
$allowed_providers = [ 'openai', 'claude', 'gemini' ];
$provider = sanitize_text_field( $request->get_param( 'provider' ) );
if ( ! in_array( $provider, $allowed_providers, true ) ) {
    $provider = get_option( 'waipg_settings' )['provider'];
}

// Options sanitization
$options = $request->get_param( 'options' );
$clean_options = [
    'tone' => sanitize_text_field( $options['tone'] ?? 'professional' ),
    'length' => sanitize_text_field( $options['length'] ?? 'medium' ),
];
```

### 7.2 Output Escaping

**Product Title**:
```php
// AI-generated titles are sanitized before saving
$generated_title = sanitize_text_field( $ai_response['title'] );
```

**Product Description**:
```php
// Use wp_kses_post to allow safe HTML
$generated_desc = wp_kses_post( $ai_response['description'] );
```

### 7.3 Nonce Verification

**REST API Middleware**:
```php
add_filter( 'rest_pre_dispatch', function( $result, $server, $request ) {
    if ( strpos( $request->get_route(), '/waipg/v1' ) === 0 ) {
        $nonce = $request->get_header( 'X-WP-Nonce' );
        if ( ! wp_verify_nonce( $nonce, 'wp_rest' ) ) {
            return new WP_Error(
                'invalid_nonce',
                __( 'Invalid security token', 'waipg' ),
                [ 'status' => 403 ]
            );
        }
    }
    return $result;
}, 10, 3 );
```

### 7.4 API Key Encryption

**Encryption Class**:
```php
class WAIPG_Encryption {
    
    private static function get_key(): string {
        return hash( 'sha256', AUTH_KEY . SECURE_AUTH_KEY );
    }
    
    private static function get_iv(): string {
        return substr( hash( 'sha256', NONCE_KEY ), 0, 16 );
    }
    
    public static function encrypt( string $data ): string {
        $key = self::get_key();
        $iv = self::get_iv();
        $encrypted = openssl_encrypt( $data, 'AES-256-CBC', $key, 0, $iv );
        return base64_encode( $encrypted );
    }
    
    public static function decrypt( string $data ): string {
        $key = self::get_key();
        $iv = self::get_iv();
        $decrypted = openssl_decrypt( base64_decode( $data ), 'AES-256-CBC', $key, 0, $iv );
        return $decrypted;
    }
}
```

**Usage**:
```php
// Saving API key
$encrypted_key = WAIPG_Encryption::encrypt( $api_key );
update_option( 'waipg_openai_api_key', $encrypted_key );

// Retrieving API key
$encrypted_key = get_option( 'waipg_openai_api_key' );
$api_key = WAIPG_Encryption::decrypt( $encrypted_key );
```

### 7.5 Rate Limiting

**Implementation**:
```php
class WAIPG_Rate_Limiter {
    
    public static function check( int $user_id, int $limit = 60 ): bool {
        $transient_key = "waipg_rate_limit_{$user_id}";
        $requests = get_transient( $transient_key ) ?: 0;
        
        if ( $requests >= $limit ) {
            return false; // Rate limit exceeded
        }
        
        set_transient( $transient_key, $requests + 1, MINUTE_IN_SECONDS );
        return true;
    }
}
```

---

## 8. Performance Optimization

### 8.1 Caching Strategy

**Template Caching**:
```php
// Cache loaded templates for 1 hour
$cache_key = 'waipg_template_' . $template_id;
$template = wp_cache_get( $cache_key );

if ( false === $template ) {
    $template = $this->load_template_from_db( $template_id );
    wp_cache_set( $cache_key, $template, '', HOUR_IN_SECONDS );
}
```

**Provider Instance Caching**:
```php
// Singleton pattern for provider instances
private static $instances = [];

public static function create( string $provider_name ): WAIPG_AI_Provider {
    if ( ! isset( self::$instances[ $provider_name ] ) ) {
        self::$instances[ $provider_name ] = new $provider_class();
    }
    return self::$instances[ $provider_name ];
}
```

### 8.2 Asset Loading Optimization

**Conditional Loading**:
```php
// Only load admin assets on plugin pages
public function enqueue_admin_scripts( $hook ) {
    $allowed_hooks = [
        'woocommerce_page_wc-settings',
        'product',
        'edit-product',
        'toplevel_page_waipg'
    ];
    
    if ( ! in_array( $hook, $allowed_hooks, true ) ) {
        return;
    }
    
    wp_enqueue_script( 'waipg-admin', /* ... */ );
}
```

**Script Dependencies**:
```php
wp_enqueue_script(
    'waipg-admin',
    WAIPG_PLUGIN_URL . 'admin/js/build/admin.js',
    [ 'react', 'react-dom', 'wp-api-fetch', 'wp-components', 'wp-i18n' ],
    WAIPG_VERSION,
    true
);
```

### 8.3 Database Query Optimization

**Batch Product Queries**:
```php
// Instead of individual queries in a loop
foreach ( $product_ids as $id ) {
    $product = wc_get_product( $id ); // ❌ N+1 query problem
}

// Batch query
$products = wc_get_products([
    'include' => $product_ids,
    'limit' => -1
]); // ✅ Single query
```

### 8.4 Background Processing

**Action Scheduler Configuration**:
```php
// Process 5 products at a time
as_schedule_recurring_action(
    time(),
    300, // Every 5 minutes
    'waipg_process_bulk_batch',
    [ 'batch_id' => $batch_id ],
    'waipg'
);

// Hook handler
add_action( 'waipg_process_bulk_batch', function( $batch_id ) {
    $batch_size = 5;
    $products = get_next_batch_products( $batch_id, $batch_size );
    
    foreach ( $products as $product_id ) {
        // Process product
        $this->generator->generate_both( $product_id );
        update_progress( $batch_id, $product_id );
    }
    
    if ( is_batch_complete( $batch_id ) ) {
        send_completion_email( $batch_id );
        as_unschedule_action( 'waipg_process_bulk_batch', [ 'batch_id' => $batch_id ] );
    }
});
```

---

## 9. Error Handling & Logging

### 9.1 Error Types

**Classification**:
1. **API Errors**: Rate limits, invalid keys, network failures
2. **Validation Errors**: Invalid product data, malformed requests
3. **System Errors**: Database failures, file permissions
4. **Business Logic Errors**: Template not found, unsupported product type

### 9.2 Logging Implementation

**Logger Class**:
```php
class WAIPG_Logger {
    
    const LOG_LEVEL_ERROR = 'error';
    const LOG_LEVEL_WARNING = 'warning';
    const LOG_LEVEL_INFO = 'info';
    const LOG_LEVEL_DEBUG = 'debug';
    
    public static function log( string $message, string $level = self::LOG_LEVEL_INFO, array $context = [] ): void {
        
        if ( ! self::should_log( $level ) ) {
            return;
        }
        
        $log_entry = [
            'timestamp' => current_time( 'mysql' ),
            'level' => $level,
            'message' => $message,
            'context' => $context,
            'user_id' => get_current_user_id(),
            'request_uri' => $_SERVER['REQUEST_URI'] ?? '',
        ];
        
        // Use WooCommerce logger if available
        if ( function_exists( 'wc_get_logger' ) ) {
            $logger = wc_get_logger();
            $logger->log( $level, wp_json_encode( $log_entry ), [ 'source' => 'waipg' ] );
        } else {
            error_log( 'WAIPG: ' . wp_json_encode( $log_entry ) );
        }
    }
    
    private static function should_log( string $level ): bool {
        $settings = get_option( 'waipg_settings', [] );
        return ! empty( $settings['enable_logging'] );
    }
}
```

**Usage Examples**:
```php
// API error
WAIPG_Logger::log(
    'OpenAI API request failed',
    WAIPG_Logger::LOG_LEVEL_ERROR,
    [
        'provider' => 'openai',
        'error_code' => 429,
        'error_message' => 'Rate limit exceeded',
        'product_id' => 123
    ]
);

// Successful generation
WAIPG_Logger::log(
    'Product title generated successfully',
    WAIPG_Logger::LOG_LEVEL_INFO,
    [
        'product_id' => 123,
        'provider' => 'claude',
        'tokens_used' => 28
    ]
);
```

### 9.3 User-Facing Error Messages

**Error Response Format**:
```php
return new WP_Error(
    'api_error',
    sprintf(
        /* translators: %s: AI provider name */
        __( 'Failed to generate content. %s API is currently unavailable. Please try again later.', 'waipg' ),
        $provider_name
    ),
    [
        'status' => 503,
        'retry_after' => 60
    ]
);
```

**Admin Notices**:
```php
add_action( 'admin_notices', function() {
    if ( $has_api_error ) {
        ?>
        <div class="notice notice-error is-dismissible">
            <p>
                <strong><?php esc_html_e( 'WooCommerce AI Product Generator', 'waipg' ); ?>:</strong>
                <?php esc_html_e( 'API key validation failed. Please check your settings.', 'waipg' ); ?>
            </p>
        </div>
        <?php
    }
});
```

---

## 10. Testing Strategy

### 10.1 Unit Tests (PHPUnit)

**Coverage Targets**:
- Provider classes: 90%+
- Generator classes: 85%+
- Template manager: 85%+
- Utilities: 90%+

**Example Test**:
```php
class WAIPG_OpenAI_Provider_Test extends WP_UnitTestCase {
    
    private $provider;
    
    public function setUp(): void {
        parent::setUp();
        $this->provider = new WAIPG_OpenAI_Provider();
        $this->provider->set_api_key( 'test-key-123' );
    }
    
    public function test_generate_returns_error_with_invalid_key(): void {
        $this->provider->set_api_key( 'invalid' );
        $result = $this->provider->generate( 'Test prompt' );
        
        $this->assertFalse( $result['success'] );
        $this->assertArrayHasKey( 'error', $result );
    }
    
    public function test_validate_credentials_with_valid_key(): void {
        // Mock HTTP response
        add_filter( 'pre_http_request', function() {
            return [
                'response' => [ 'code' => 200 ],
                'body' => json_encode([ 'data' => [] ])
            ];
        });
        
        $result = $this->provider->validate_credentials();
        $this->assertTrue( $result['valid'] );
    }
}
```

### 10.2 Integration Tests

**Test Scenarios**:
1. Full generation workflow (product → template → provider → save)
2. Bulk processing with Action Scheduler
3. REST API endpoints with authentication
4. Template variable substitution
5. Error recovery and retry logic

### 10.3 React Component Tests (Jest)

**Example Test**:
```javascript
import { render, fireEvent, waitFor } from '@testing-library/react';
import GeneratorPanel from '../components/GeneratorPanel';

describe('GeneratorPanel', () => {
    it('should generate title on button click', async () => {
        const { getByText, getByRole } = render(
            <GeneratorPanel productId={123} />
        );
        
        const generateButton = getByRole('button', { name: /generate title/i });
        fireEvent.click(generateButton);
        
        await waitFor(() => {
            expect(getByText(/successfully generated/i)).toBeInTheDocument();
        });
    });
    
    it('should show error message on API failure', async () => {
        // Mock API error
        global.fetch = jest.fn(() =>
            Promise.resolve({
                ok: false,
                json: () => Promise.resolve({ error: 'API error' })
            })
        );
        
        const { getByText, getByRole } = render(
            <GeneratorPanel productId={123} />
        );
        
        const generateButton = getByRole('button', { name: /generate title/i });
        fireEvent.click(generateButton);
        
        await waitFor(() => {
            expect(getByText(/failed to generate/i)).toBeInTheDocument();
        });
    });
});
```

### 10.4 E2E Tests (Playwright/Puppeteer)

**Test Scenarios**:
1. Install and activate plugin
2. Configure API settings
3. Generate content for single product
4. Run bulk generation
5. Monitor progress
6. Verify generated content saved correctly

---

## 11. Internationalization (i18n)

### 11.1 Text Domain Setup

**Main Plugin File**:
```php
load_plugin_textdomain(
    'woocommerce-ai-product-generator',
    false,
    dirname( plugin_basename( __FILE__ ) ) . '/languages'
);
```

### 11.2 String Translation

**PHP**:
```php
__( 'Generate Title', 'woocommerce-ai-product-generator' );
_e( 'Settings saved successfully', 'woocommerce-ai-product-generator' );
esc_html_e( 'AI Provider', 'woocommerce-ai-product-generator' );

// With placeholders
sprintf(
    /* translators: %d: number of products */
    _n(
        '%d product processed',
        '%d products processed',
        $count,
        'woocommerce-ai-product-generator'
    ),
    $count
);
```

**JavaScript**:
```javascript
import { __ } from '@wordpress/i18n';

const title = __( 'Generate Title', 'woocommerce-ai-product-generator' );
```

### 11.3 POT File Generation

**Build Script**:
```bash
wp i18n make-pot . languages/woocommerce-ai-product-generator.pot \
    --domain=woocommerce-ai-product-generator \
    --exclude=node_modules,vendor,tests
```

---

## 12. Deployment & Release

### 12.1 Build Process

**Production Build**:
```bash
# Install dependencies
composer install --no-dev --optimize-autoloader
npm ci --production

# Build assets
npm run build

# Generate POT file
npm run i18n

# Create ZIP
composer archive --format=zip --file=woocommerce-ai-product-generator
```

**package.json scripts**:
```json
{
  "scripts": {
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production",
    "i18n": "wp i18n make-pot . languages/woocommerce-ai-product-generator.pot",
    "test": "jest",
    "test:php": "phpunit"
  }
}
```

### 12.2 WordPress.org Submission

**Checklist**:
- [ ] Plugin adheres to WordPress.org guidelines
- [ ] No hardcoded credentials or API keys
- [ ] GPL-compatible license
- [ ] Readme.txt properly formatted
- [ ] Screenshots prepared (1280x960px)
- [ ] Plugin icon (256x256px, 128x128px)
- [ ] Plugin banner (1544x500px, 772x250px)
- [ ] All strings translatable
- [ ] No PHP errors or warnings
- [ ] Security review passed
- [ ] Accessibility review passed

**readme.txt Structure**:
```
=== WooCommerce AI Product Generator ===
Contributors: yourusername
Tags: woocommerce, ai, product description, openai, claude
Requires at least: 6.0
Tested up to: 6.5
Requires PHP: 7.4
Stable tag: 1.0.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

Generate compelling product titles and descriptions using AI.

== Description ==
[Full description...]

== Installation ==
[Installation steps...]

== Frequently Asked Questions ==
[FAQ items...]

== Screenshots ==
1. Settings page
2. Single product generator
3. Bulk generation interface

== Changelog ==
= 1.0.0 =
* Initial release
```

### 12.3 Versioning Strategy

**Semantic Versioning** (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes, incompatible API updates
- **MINOR**: New features, backward-compatible
- **PATCH**: Bug fixes, security patches

**Release Schedule**:
- Major releases: Quarterly
- Minor releases: Monthly
- Patch releases: As needed

### 12.4 Update Mechanism

**Plugin Update Checker**:
```php
add_filter( 'pre_set_site_transient_update_plugins', function( $transient ) {
    // Check for updates from WordPress.org
    // Or custom update server for pro version
    return $transient;
});
```

---

## 13. Documentation Plan

### 13.1 User Documentation

**Admin Guide** (GitBook/Docs site):
1. Getting Started
   - Installation
   - Initial Setup
   - API Key Configuration
2. Using the Plugin
   - Single Product Generation
   - Bulk Generation
   - Template Management
3. Advanced Features
   - Custom Templates
   - Category-Specific Settings
   - Automation Rules
4. Troubleshooting
   - Common Errors
   - API Issues
   - Performance Tips

### 13.2 Developer Documentation

**Technical Docs**:
1. Architecture Overview
2. Extending the Plugin
   - Creating Custom Providers
   - Adding Template Variables
   - Hooks & Filters Reference
3. API Reference
   - REST Endpoints
   - PHP Classes
   - JavaScript API
4. Contributing Guide
   - Code Standards
   - Testing Requirements
   - Pull Request Process

### 13.3 Inline Code Documentation

**PHPDoc Standards**:
```php
/**
 * Generate product description using AI
 *
 * Extracts product data, applies template, sends to AI provider,
 * and returns formatted description ready for saving.
 *
 * @since 1.0.0
 *
 * @param int   $product_id WooCommerce product ID.
 * @param array $options {
 *     Optional. Generation options.
 *
 *     @type string $tone        Tone of voice (professional, casual, creative).
 *     @type string $length      Length of description (short, medium, long).
 *     @type array  $keywords    Keywords to include in description.
 *     @type bool   $include_seo Whether to optimize for SEO.
 * }
 * @return array {
 *     Generation result.
 *
 *     @type bool   $success     Whether generation succeeded.
 *     @type string $description Generated description HTML.
 *     @type string $error       Error message if failed.
 *     @type int    $tokens      Number of tokens used.
 * }
 *
 * @throws WAIPG_Exception If product doesn't exist or API fails.
 */
public function generate_description( int $product_id, array $options = [] ): array {
    // Implementation
}
```

---

## 14. Maintenance & Support Plan

### 14.1 Support Channels

1. **WordPress.org Support Forum**
   - Monitor daily
   - Response time: < 24 hours
   - Community-driven support

2. **GitHub Issues**
   - Bug reports
   - Feature requests
   - Technical discussions

3. **Documentation Site**
   - Self-service knowledge base
   - Video tutorials
   - FAQ updates

### 14.2 Monitoring

**Error Tracking**:
- Integrate with Sentry or similar
- Track JavaScript errors
- Monitor API failures
- Alert on critical issues

**Usage Analytics** (opt-in):
- Active installations
- Popular features
- Error rates
- Performance metrics

### 14.3 Update Cycle

**Monthly Updates**:
- WordPress/WooCommerce compatibility
- Security patches
- Minor bug fixes

**Quarterly Updates**:
- New features
- UI improvements
- Performance optimizations

---

## 15. Technical Debt & Future Enhancements

### 15.1 Known Limitations (v1.0)

1. No support for variable products (coming in v1.1)
2. Limited to 3 AI providers (extensible architecture)
3. Basic template system (visual editor planned for v1.2)
4. No A/B testing for generated content
5. No multilingual support (WPML integration planned)

### 15.2 Roadmap

**v1.1 (Q3 2026)**:
- Variable product support
- Azure OpenAI provider
- Advanced template conditionals
- Webhook integration

**v1.2 (Q4 2026)**:
- Visual template editor
- A/B testing for generated content
- Performance analytics dashboard
- WPML integration

**v2.0 (Q1 2027)**:
- Multi-language generation
- Image generation integration
- Custom fine-tuning support
- Pro version features

---

## 16. Risk Assessment & Mitigation

### 16.1 Identified Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AI API rate limits | High | Medium | Implement queue system, retry logic |
| API cost overruns | Medium | High | Usage caps, cost estimation, warnings |
| API key theft | Low | Critical | Encryption, HTTPS-only, audit logging |
| Plugin conflicts | Medium | Medium | Namespace isolation, WordPress standards |
| Performance issues | Medium | Medium | Background processing, caching |
| API changes | Medium | High | Version pinning, adapter pattern |

### 16.2 Mitigation Strategies

**Rate Limit Protection**:
```php
// Exponential backoff retry
$max_retries = 3;
$retry_delay = 2; // seconds

for ( $i = 0; $i < $max_retries; $i++ ) {
    $result = $provider->generate( $prompt );
    
    if ( $result['success'] ) {
        break;
    }
    
    if ( isset( $result['error_code'] ) && 429 === $result['error_code'] ) {
        sleep( $retry_delay * ( 2 ** $i ) ); // 2s, 4s, 8s
        continue;
    }
    
    break; // Non-rate-limit error
}
```

**Cost Controls**:
```php
// Monthly usage cap
$monthly_usage = get_option( 'waipg_monthly_tokens', 0 );
$monthly_cap = get_option( 'waipg_settings' )['monthly_token_cap'] ?? 100000;

if ( $monthly_usage >= $monthly_cap ) {
    return new WP_Error(
        'usage_cap_exceeded',
        __( 'Monthly usage cap exceeded. Please increase your limit or wait until next month.', 'waipg' )
    );
}
```

---

## 17. Success Metrics

### 17.1 Technical KPIs

- **Performance**:
  - Single generation: < 5 seconds (p95)
  - API success rate: > 98%
  - Admin page load: < 2 seconds
  
- **Reliability**:
  - Uptime: > 99.5%
  - Error rate: < 2%
  - Failed job retry success: > 90%

- **Code Quality**:
  - Test coverage: > 80%
  - PHPCS violations: 0
  - Security vulnerabilities: 0

### 17.2 Business KPIs

- **Adoption**:
  - 1,000 active installations in 6 months
  - 5,000 active installations in 12 months
  - 4+ star average rating

- **Engagement**:
  - 70%+ of users generate content within first week
  - Average 100 generations per user per month
  - < 5% uninstall rate

- **Support**:
  - < 24 hour response time
  - > 80% resolution rate
  - < 10 active support tickets at any time

---

## 18. Development Timeline

### Phase 1: Foundation (Weeks 1-2)
- Project setup and boilerplate
- AI provider interface and factory
- Settings framework
- REST API foundation

### Phase 2: Core Features (Weeks 3-5)
- OpenAI, Claude, Gemini providers
- Product generator implementation
- Template system
- Single product generation UI

### Phase 3: Bulk Processing (Week 6)
- Action Scheduler integration
- Queue management
- Progress tracking
- Bulk UI

### Phase 4: Polish & Testing (Weeks 7-8)
- React component refinement
- Comprehensive testing
- Security audit
- Performance optimization

### Phase 5: Documentation (Week 9)
- User documentation
- Developer documentation
- Video tutorials
- Marketing materials

### Phase 6: Beta & Release (Weeks 10-12)
- Private beta testing
- Bug fixes and refinements
- WordPress.org submission
- Public launch

**Total Timeline**: 12 weeks (3 months)

---

## 19. Resource Requirements

### 19.1 Development Team

- **Lead Developer**: 1 FTE (full-stack: PHP + React)
- **QA Engineer**: 0.5 FTE
- **Technical Writer**: 0.25 FTE
- **Designer** (UI/UX): 0.25 FTE (for admin interface)

### 19.2 Infrastructure

- **Development**:
  - Local WordPress/WooCommerce environment
  - Git repository (GitHub)
  - CI/CD pipeline (GitHub Actions)

- **Testing**:
  - Staging server (WordPress/WooCommerce)
  - API sandboxes (OpenAI, Claude, Gemini)
  - Browser testing (BrowserStack)

- **Production** (Post-Launch):
  - WordPress.org hosting (free)
  - Documentation site (GitHub Pages or GitBook)
  - Error tracking (Sentry)
  - Analytics (opt-in, privacy-focused)

### 19.3 Budget Estimate

- **Development**: $30,000 - $40,000 (based on 12 weeks, team composition)
- **API Credits** (testing): $500 - $1,000
- **Tools & Services**: $1,000 - $2,000
- **Marketing**: $2,000 - $5,000

**Total**: $33,500 - $48,000

---

## 20. Appendices

### Appendix A: WordPress Coding Standards Reference
- [PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/)
- [JavaScript Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/javascript/)
- [Accessibility Guidelines](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/)

### Appendix B: AI Provider Documentation
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference)
- [Google Gemini API](https://ai.google.dev/docs)

### Appendix C: WooCommerce Resources
- [WooCommerce Developer Documentation](https://woocommerce.com/document/create-a-plugin/)
- [Action Scheduler Documentation](https://actionscheduler.org/)
- [WooCommerce REST API](https://woocommerce.github.io/woocommerce-rest-api-docs/)

### Appendix D: Glossary

- **SDD**: Spec-Driven Development
- **WAIPG**: WooCommerce AI Product Generator (plugin prefix)
- **TTL**: Time To Live (cache duration)
- **WPCS**: WordPress Coding Standards
- **i18n**: Internationalization
- **WP-CLI**: WordPress Command Line Interface

---

## Document Control

**Version**: 1.0  
**Last Updated**: April 9, 2026  
**Author**: Claude (AI Assistant)  
**Reviewed By**: [To be assigned]  
**Next Review Date**: May 9, 2026

**Change Log**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-09 | Claude | Initial technical plan created |

---

**End of Technical Implementation Plan**