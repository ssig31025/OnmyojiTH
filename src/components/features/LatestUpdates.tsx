import Link from "next/link";
import { ArrowRight, Calendar } from "lucide-react";

const updates = [
    {
        id: 1,
        title: "New SSR Shikigami: Amaterasu Arrives",
        date: "2023-10-25",
        category: "New Arrival",
    },
    {
        id: 2,
        title: "Patch Notes: Skill Balance Adjustments",
        date: "2023-10-18",
        category: "Patch Notes",
    },
    {
        id: 3,
        title: "Event Guide: Six Realms Gate",
        date: "2023-10-15",
        category: "Event",
    },
];

export function LatestUpdates() {
    return (
        <section className="container py-12 md:py-16 border-t">
            <div className="flex items-center justify-between mb-8">
                <h2 className="text-2xl font-bold tracking-tight">Latest Updates</h2>
                <Link href="/news" className="text-sm font-medium text-primary hover:underline flex items-center">
                    View All <ArrowRight className="ml-1 h-4 w-4" />
                </Link>
            </div>

            <div className="grid gap-4 md:grid-cols-3">
                {updates.map((update) => (
                    <Link
                        key={update.id}
                        href={`/news/${update.id}`}
                        className="group block space-y-3 rounded-lg border p-5 transition-colors hover:bg-muted/50"
                    >
                        <div className="flex items-center gap-2 text-xs text-muted-foreground">
                            <span className="rounded-full bg-primary/10 px-2 py-0.5 text-primary font-medium">
                                {update.category}
                            </span>
                            <span className="flex items-center">
                                <Calendar className="mr-1 h-3 w-3" />
                                {update.date}
                            </span>
                        </div>
                        <h3 className="font-semibold leading-tight group-hover:text-primary transition-colors">
                            {update.title}
                        </h3>
                    </Link>
                ))}
            </div>
        </section>
    );
}
