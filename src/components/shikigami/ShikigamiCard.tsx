import Link from "next/link";
import { Shikigami } from "@/types/shikigami";
import { Badge } from "@/components/ui/badge";

interface ShikigamiCardProps {
    data: Shikigami;
}

const rarityColors: Record<string, string> = {
    SP: "bg-red-600 text-white border-red-400",
    SSR: "bg-orange-500 text-white border-orange-300",
    SR: "bg-purple-500 text-white border-purple-300",
    R: "bg-blue-500 text-white border-blue-300",
    N: "bg-gray-500 text-white border-gray-300",
    SSN: "bg-pink-500 text-white border-pink-300",
    UR: "bg-indigo-600 text-white border-indigo-400",
};

export function ShikigamiCard({ data }: ShikigamiCardProps) {
    return (
        <Link href={`/shikigami/${data.id}`} className="group block">
            <div className="relative overflow-hidden rounded-xl border bg-card transition-all hover:shadow-lg hover:-translate-y-1">
                <div className="aspect-square bg-muted flex items-center justify-center text-muted-foreground relative">
                    {data.icon || data.image ? (
                        <img
                            src={data.icon || data.image}
                            alt={data.name}
                            className="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105"
                        />
                    ) : (
                        <span className="text-4xl font-bold opacity-20">{data.name[0]}</span>
                    )}
                </div>

                <div className="p-4">
                    <div className="flex items-center justify-between mb-2">
                        <Badge variant="outline" className={`${rarityColors[data.rarity]} font-bold`}>
                            {data.rarity}
                        </Badge>
                    </div>
                    <h3 className="font-bold text-lg group-hover:text-primary transition-colors">
                        {data.name}
                    </h3>
                    <div className="flex gap-1 mt-2">
                        {data.role.map((role) => (
                            <span key={role} className="text-xs text-muted-foreground bg-muted px-2 py-0.5 rounded">
                                {role}
                            </span>
                        ))}
                    </div>
                </div>
            </div>
        </Link>
    );
}
