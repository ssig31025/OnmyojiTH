import Link from "next/link";

export function Footer() {
    return (
        <footer className="border-t bg-muted/40">
            <div className="container py-8 md:py-12">
                <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
                    <div className="space-y-3">
                        <h3 className="text-lg font-bold">OnmyojiDB</h3>
                        <p className="text-sm text-muted-foreground">
                            The ultimate database and toolset for Onmyoji players. Built by fans, for fans.
                        </p>
                    </div>

                    <div>
                        <h4 className="font-semibold mb-3">Database</h4>
                        <ul className="space-y-2 text-sm text-muted-foreground">
                            <li><Link href="/shikigami" className="hover:text-primary">All Shikigami</Link></li>
                            <li><Link href="/souls" className="hover:text-primary">Soul Library</Link></li>
                            <li><Link href="/mechanics" className="hover:text-primary">Game Mechanics</Link></li>
                        </ul>
                    </div>

                    <div>
                        <h4 className="font-semibold mb-3">Tools</h4>
                        <ul className="space-y-2 text-sm text-muted-foreground">
                            <li><Link href="/tools/team-builder" className="hover:text-primary">Team Builder</Link></li>
                            <li><Link href="/tools/speed" className="hover:text-primary">Speed Calculator</Link></li>
                            <li><Link href="/tools/damage" className="hover:text-primary">Damage Sim</Link></li>
                        </ul>
                    </div>

                    <div>
                        <h4 className="font-semibold mb-3">Legal</h4>
                        <ul className="space-y-2 text-sm text-muted-foreground">
                            <li><Link href="/privacy" className="hover:text-primary">Privacy Policy</Link></li>
                            <li><Link href="/terms" className="hover:text-primary">Terms of Service</Link></li>
                        </ul>
                    </div>
                </div>

                <div className="mt-8 pt-8 border-t text-center text-xs text-muted-foreground">
                    <p>&copy; {new Date().getFullYear()} OnmyojiDB. Not affiliated with NetEase Games.</p>
                    <p className="mt-1">Onmyoji and all related assets are trademarks of NetEase Games.</p>
                </div>
            </div>
        </footer>
    );
}
