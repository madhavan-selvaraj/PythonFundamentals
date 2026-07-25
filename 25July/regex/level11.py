import re

text1 = "apple,banana,mango,orange,grapes"

text2 = "apple,banana;mango,orange;grapes,kiwi"

text3 = "Python    regex   is     very   useful    for   text    processing"

text4 = "apple,banana; mango orange,grapes;kiwi  watermelon"

new1 = re.split(r",", text1)  # Split using commas.

new2 = re.split(r"[\,,\;]", text2)  # Split using commas or semicolons.

new3 = re.split(
    r"\s+", text3
)  # Split a sentence into words regardless of multiple spaces

new4 = re.split(r"[,;\s]+", text4)  # Split using commas, semicolons, or spaces
