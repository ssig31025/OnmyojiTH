import type { NextConfig } from "next";

const isProd = process.env.NODE_ENV === 'production';
const repoName = "OnmyojiTH";

const nextConfig: NextConfig = {
  /* config options here */
  output: "export",
  images: {
    unoptimized: true,
  },
  basePath: isProd ? `/${repoName}` : "",
  trailingSlash: true,
  reactCompiler: true,
};

export default nextConfig;
