import { getAllShikigami, getShikigamiById } from "@/lib/data/shikigami";
import { SkillCard } from "@/components/shikigami/SkillCard";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { ArrowLeft, Shield, Sword, Zap, Heart, Wind } from "lucide-react";
import { notFound } from "next/navigation";

// Required for static export
export function generateStaticParams() {
  const shikigami = getAllShikigami();
  return shikigami.map((s) => ({
    id: s.id,
  }));
}

export default async function ShikigamiDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const shikigami = getShikigamiById(id);

  if (!shikigami) {
    notFound();
  }

  return (
    <div className="min-h-screen pb-20">
      {/* Hero Header */}
      <div className="bg-muted/30 border-b">
        <div className="container py-8 md:py-12">
          <Link href="/shikigami" className="inline-flex items-center text-sm text-muted-foreground hover:text-primary mb-6">
            <ArrowLeft className="mr-2 h-4 w-4" /> Back to Library
          </Link>

          <div className="flex flex-col md:flex-row gap-8 items-start">
            <div className="w-32 h-32 md:w-40 md:h-40 rounded-xl bg-muted flex items-center justify-center shrink-0 border-2 border-primary/20 overflow-hidden">
              {shikigami.image || shikigami.icon ? (
                <img
                  src={shikigami.image || shikigami.icon}
                  alt={shikigami.name}
                  className="h-full w-full object-cover"
                />
              ) : (
                <span className="text-4xl font-bold opacity-20">{shikigami.name[0]}</span>
              )}
            </div>

            <div className="flex-1 space-y-4">
              <div className="flex items-center gap-3">
                <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight">{shikigami.name}</h1>
                <Badge className="text-lg px-3 py-1 bg-primary text-primary-foreground">
                  {shikigami.rarity}
                </Badge>
              </div>

              <div className="flex flex-wrap gap-2">
                {shikigami.role.map((role) => (
                  <Badge key={role} variant="outline" className="text-sm">
                    {role}
                  </Badge>
                ))}
              </div>

              <p className="text-lg text-muted-foreground max-w-2xl leading-relaxed">
                {shikigami.bio}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="container grid md:grid-cols-[300px_1fr] gap-8 py-12">
        {/* Sidebar: Stats */}
        <div className="space-y-6">
          <div className="rounded-xl border bg-card p-6">
            <h3 className="font-bold text-xl mb-4 flex items-center">
              <Zap className="mr-2 h-5 w-5 text-yellow-500" /> Base Stats
            </h3>
            <div className="space-y-4">
              <StatRow label="Attack" value={shikigami.stats.attack} icon={<Sword className="h-4 w-4" />} />
              <StatRow label="Health" value={shikigami.stats.health} icon={<Heart className="h-4 w-4" />} />
              <StatRow label="Defense" value={shikigami.stats.defense} icon={<Shield className="h-4 w-4" />} />
              <StatRow label="Speed" value={shikigami.stats.speed} icon={<Wind className="h-4 w-4" />} />
              <StatRow label="Crit" value={shikigami.stats.crit} icon={<Zap className="h-4 w-4" />} />
              <StatRow label="Crit DMG" value={shikigami.stats.critDmg} icon={<Zap className="h-4 w-4 text-red-500" />} />
              <StatRow label="Effect HIT" value={shikigami.stats.effectHit} icon={<Zap className="h-4 w-4 text-blue-500" />} />
              <StatRow label="Effect RES" value={shikigami.stats.effectRes} icon={<Shield className="h-4 w-4 text-green-500" />} />
            </div>
          </div>

          <div className="rounded-xl border bg-card p-6">
            <h3 className="font-bold text-lg mb-4">Quick Actions</h3>
            <div className="space-y-3">
              <Button className="w-full" variant="outline">View Skins</Button>
              <Button className="w-full" variant="outline">Soul Guide</Button>
            </div>
          </div>
        </div>

        {/* Main Content: Skills */}
        <div className="space-y-8">
          <div>
            <h2 className="text-2xl font-bold tracking-tight mb-6">Skills</h2>
            <div className="grid gap-6">
              {shikigami.skills.length > 0 ? (
                shikigami.skills.map((skill, index) => (
                  <SkillCard key={index} skill={skill} />
                ))
              ) : (
                <p className="text-muted-foreground italic">Skill data coming soon...</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function StatRow({ label, value, icon }: { label: string; value: string; icon: React.ReactNode }) {
  const getGradeColor = (grade: string) => {
    if (grade.includes("S")) return "text-yellow-500 font-bold"; // Gold for SS, S
    if (grade.includes("A")) return "text-purple-500 font-bold"; // Purple for A
    if (grade.includes("B")) return "text-blue-500 font-bold";   // Blue for B
    if (grade.includes("C")) return "text-green-500 font-bold";  // Green for C
    if (grade.includes("D")) return "text-gray-500 font-bold";   // Gray for D
    return "text-muted-foreground";
  };

  return (
    <div className="flex items-center justify-between border-b pb-2 last:border-0 last:pb-0">
      <div className="flex items-center gap-2 text-sm text-muted-foreground">
        {icon}
        {label}
      </div>
      <span className={`font-mono ${getGradeColor(value)}`}>{value}</span>
    </div>
  );
}
