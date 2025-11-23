"use client";

import { useState } from "react";
import { getAllShikigami } from "@/lib/data/shikigami";
import { ShikigamiCard } from "@/components/shikigami/ShikigamiCard";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Search, X } from "lucide-react";

export default function ShikigamiListPage() {
    const allShikigami = getAllShikigami();
    const [search, setSearch] = useState("");
    const [filterRarity, setFilterRarity] = useState<string | null>(null);

    const filtered = allShikigami.filter((s) => {
        const matchesSearch = s.name.toLowerCase().includes(search.toLowerCase());
        const matchesRarity = filterRarity ? s.rarity === filterRarity : true;
        return matchesSearch && matchesRarity;
    });

    const rarities = ["SP", "SSR", "SR", "R", "N"];

    return (
        <div className="container py-8 md:py-12">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                <div>
                    <h1 className="text-3xl font-bold tracking-tight">Shikigami Library</h1>
                    <p className="text-muted-foreground">
                        Browse and search for your favorite Shikigami.
                    </p>
                </div>
                <div className="flex flex-col sm:flex-row gap-2 w-full md:w-auto">
                    <div className="relative w-full sm:w-64">
                        <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                        <Input
                            placeholder="Search by name..."
                            className="pl-9"
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                        />
                    </div>
                </div>
            </div>

            {/* Rarity Filter */}
            <div className="flex flex-wrap gap-2 mb-8">
                <Button
                    variant={filterRarity === null ? "default" : "outline"}
                    onClick={() => setFilterRarity(null)}
                    size="sm"
                >
                    All
                </Button>
                {rarities.map((rarity) => (
                    <Button
                        key={rarity}
                        variant={filterRarity === rarity ? "default" : "outline"}
                        onClick={() => setFilterRarity(rarity)}
                        size="sm"
                    >
                        {rarity}
                    </Button>
                ))}
            </div>

            {/* Grid */}
            {filtered.length > 0 ? (
                <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-6">
                    {filtered.map((shikigami) => (
                        <ShikigamiCard key={shikigami.id} data={shikigami} />
                    ))}
                </div>
            ) : (
                <div className="text-center py-20 border rounded-lg bg-muted/20">
                    <p className="text-muted-foreground">No Shikigami found matching your criteria.</p>
                    <Button
                        variant="link"
                        onClick={() => { setSearch(""); setFilterRarity(null); }}
                        className="mt-2"
                    >
                        Clear filters
                    </Button>
                </div>
            )}
        </div>
    );
}
