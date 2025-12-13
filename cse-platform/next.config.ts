import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  output: 'standalone', // Required for Docker deployment
  compress: true,
  poweredByHeader: false,
  
  // Image optimization for production
  images: {
    unoptimized: false,
    remotePatterns: [],
  },
  
  // Environment variables
  env: {
    NEXT_PUBLIC_APP_NAME: 'DBMS Learning Platform',
  },
};

export default nextConfig;
