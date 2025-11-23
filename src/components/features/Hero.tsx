import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

export function Hero() {
    return (
        <section className="relative overflow-hidden bg-background py-20 md:py-32">
            <div className="container relative z-10 flex flex-col items-center text-center">
                <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl md:text-6xl lg:text-7xl">
                    Master the Art of <span className="text-primary">Onmyoji</span>
                </h1>
                <p className="mt-6 max-w-2xl text-lg text-muted-foreground sm:text-xl">
                    The most comprehensive database for Shikigami, Souls, and Strategy.
                    Built for the global community.
                </p>
                <div className="mt-10 flex gap-4">
                    <Button asChild size="lg" className="h-12 px-8 text-base">
                        <Link href="/shikigami">
                            Explore Shikigami <ArrowRight className="ml-2 h-4 w-4" />
                        </Link>
                    </Button>
                    <Button asChild variant="outline" size="lg" className="h-12 px-8 text-base">
                        <Link href="/tools/team-builder">
                            Build Team
                        </Link>
                    </Button>
                </div>
            </div>

            {/* Decorative background elements */}
            <div className="absolute top-1/2 left-1/2 -z-10 h-[500px] w-[500px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary/5 blur-3xl" />
        </section>
    );
}
