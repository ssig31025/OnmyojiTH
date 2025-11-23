import { Skill } from "@/types/shikigami";
import { Badge } from "@/components/ui/badge";

interface SkillCardProps {
    skill: Skill;
}

import Image from "next/image";

// ...

export function SkillCard({ skill }: SkillCardProps) {
    const isProd = process.env.NODE_ENV === 'production';
    const basePath = isProd ? '/OnmyojiTH' : '';

    // Fix image paths in description for GitHub Pages
    const processedDescription = skill.description.replace(/src="\/images/g, `src="${basePath}/images`);

    return (
        <div className="rounded-lg border bg-card p-4 md:p-6">
            <div className="flex items-start gap-4">
                <div className="h-12 w-12 shrink-0 rounded bg-muted flex items-center justify-center overflow-hidden border relative">
                    {skill.icon ? (
                        <Image
                            src={skill.icon}
                            alt={skill.name}
                            fill
                            className="object-cover"
                        />
                    ) : (
                        <span className="text-xs font-bold text-muted-foreground">ICON</span>
                    )}
                </div>
                <div className="flex-1 space-y-1">
                    <div className="flex items-center justify-between">
                        <h3 className="font-bold">{skill.name}</h3>
                    </div>
                    <div className="text-sm text-muted-foreground mt-1">
                        <span className="mr-3">Type: <span className="font-medium text-foreground">{skill.type}</span></span>
                        <span className="mr-3">Onibi: <span className="font-medium text-foreground">{skill.orbCost}</span></span>
                        <span>Cooldown: <span className="font-medium text-foreground">0</span></span>
                    </div>
                    <div
                        className="text-sm mt-2 leading-relaxed whitespace-pre-wrap [&>img]:inline-block [&>img]:h-5 [&>img]:w-5 [&>img]:align-sub [&>img]:mx-1"
                        dangerouslySetInnerHTML={{ __html: processedDescription }}
                    />

                    {skill.levelUpEffects.length > 0 && (
                        <div className="mt-4 space-y-2 border-t pt-3">
                            <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">Level Up Effects</p>
                            <ul className="space-y-1">
                                {skill.levelUpEffects.map((effect) => (
                                    <li key={effect.level} className="text-xs text-muted-foreground">
                                        <span className="font-medium text-foreground">Lv. {effect.level}:</span> {effect.description}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
