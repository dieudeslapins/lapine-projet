#ifndef MINECRAFT_SAMPLE_LIGHTMAP_GLSL
#define MINECRAFT_SAMPLE_LIGHTMAP_GLSL

// Fullbright "Lapine" : on garde 10 % de l'eclairage d'origine pour
// conserver un leger relief, et on remonte le reste a pleine luminosite.
// Resultat : on voit la nuit et dans les grottes, sans commande ni mod.
vec4 sample_lightmap(sampler2D lightMap, ivec2 uv) {
    vec4 lightmap = texture(lightMap, clamp((uv / 256.0) + 0.5 / 16.0, vec2(0.5 / 16.0), vec2(15.5 / 16.0)));
    return mix(lightmap, vec4(1.0), 0.90);
}

#endif
