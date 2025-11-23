import { Hero } from "@/components/features/Hero";
import { FeatureGrid } from "@/components/features/FeatureGrid";
import { LatestUpdates } from "@/components/features/LatestUpdates";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Hero />
      <FeatureGrid />
      <LatestUpdates />
    </div>
  );
}
