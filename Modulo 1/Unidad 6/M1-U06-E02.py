# Ejemplo 2
import re

sentence = "¡Oh amor mío, esposa mía! La muerte, que ha extraído la miel de tu aliento, no ha tenido poder aún sobre tu hermosura; no has sido vencida; el carmín, distintivo de la belleza, luce en tus labios y mejillas, do aún no ondea la pálida enseña de la muerte. -¡Oh, Julieta!, ¿por qué luces tan encantadora todavía? -Aquí, aquí voy a establecer mi eternal permanencia, a sacudir del yugo de las estrellas enemigas este cuerpo cansado de vivir."

matches = re.findall(r'\ba\w+',sentence)

print(matches)