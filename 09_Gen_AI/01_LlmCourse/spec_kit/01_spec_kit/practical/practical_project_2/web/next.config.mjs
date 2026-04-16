/** @type {import('next').NextConfig} */
const requiredEnvVars = ["NEXT_PUBLIC_API_URL"];
for (const envVar of requiredEnvVars) {
  if (!process.env[envVar]) {
    throw new Error(
      `Missing required environment variable: ${envVar}\n` +
        `Set it in your .env.local file or CI environment.`
    );
  }
}

const nextConfig = {
  // output: "standalone" is deferred to Phase 9 production hardening
};

export default nextConfig;
