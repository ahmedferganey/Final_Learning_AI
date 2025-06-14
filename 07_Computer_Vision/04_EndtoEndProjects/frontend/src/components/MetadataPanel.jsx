function MetadataPanel({ metadata }) {
  return (
    <div>
      <h3>Metadata</h3>
      <pre>{JSON.stringify(metadata, null, 2)}</pre>
      {metadata.violations?.length > 0 && (
        <div style={{ color: 'red' }}>
          🚨 {metadata.violations.length} Violation(s) Detected!
        </div>
      )}
    </div>
  );
}

export default MetadataPanel; // ✅ Add this line
