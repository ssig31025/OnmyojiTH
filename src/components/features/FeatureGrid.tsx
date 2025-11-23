import Link from "next/link";
import { Users, Disc, Sword, Calculator } from "lucide-react";

const features = [
    {
        title: "Shikigami Library",
        description: "Detailed stats, skills, and evolution materials for all characters.",
        icon: Users,
        href: "/shikigami",
        color: "text-blue-500",
    },
    {
        title: "Soul Database",
        description: "Complete catalog of souls with drop locations and set effects.",
        icon: Disc,
        href: "/souls",
        color: "text-purple-500",
    },
    {
        title: "Game Modes",
        description: "Guides for Secret Zones, Assembly Bosses, and PvP Duel.",
        icon: Sword,
        href: "/modes",
        color: "text-red-500",
    },
    {
        title: "Tools & Calcs",
        description: "Team builder, speed tuner, and damage calculators.",
        icon: Calculator,
        href: "/tools",
        color: "text-green-500",
    },
];

export function FeatureGrid() {
    return (
        <section className="container py-12 md:py-16">
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                {features.map((feature) => (
                    <Link
                        key={feature.title}
                        href={feature.href}
                        className="group relative overflow-hidden rounded-lg border bg-card p-6 transition-all hover:shadow-md hover:border-primary/50"
                    >
                        <div className="flex flex-col gap-4">
                            <div className={`p-2 w-fit rounded-md bg-muted ${feature.color}`}>
                                <feature.icon className="h-6 w-6" />
                            </div>
                            <div className="space-y-2">
                                <h3 className="font-bold leading-none tracking-tight group-hover:text-primary transition-colors">
                                    {feature.title}
                                </h3>
                                <p className="text-sm text-muted-foreground">
                                    {feature.description}
                                </p>
                            </div>
                        </div>
                    </Link>
                ))}
            </div>
        </section>
    );
}
