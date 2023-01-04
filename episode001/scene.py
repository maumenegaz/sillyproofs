from manim import *

class SillyProofs(Scene):
    def construct(self):
        text = Text("Welcome to silly proofs\nProof #1",
                    gradient = (RED, GREEN, BLUE),
                    font_size = 60)
        
        self.play(Write(text), runtime = 3)
        self.wait(3)
        self.play(FadeOut(text))


class Theorem(Scene):
    def construct(self):
        self.math_font_size = 40

        text1 = Tex("Theorem",
                    color = WHITE,
                    font_size = self.math_font_size)
        
        math1 = Tex("Let  $\\ln x$ be the natural logarithm function.",
                    color = WHITE,
                    font_size = self.math_font_size)

        math2 = Tex("Then:",
                    color = WHITE,
                    font_size = self.math_font_size)
        
        math3 = Tex("$\\dfrac{d}{dx}\\ln x = \\dfrac{1}{x}$.",
                    color = WHITE,
                    font_size = self.math_font_size)

        VGroup(text1, math1, math2, math3).arrange(DOWN, aligned_edge = LEFT)

        self.play(Write(text1), runtime = 7)
        self.play(Write(math1), runtime = 7)
        self.play(Write(math2), runtime = 7)
        self.play(Write(math3), runtime = 7)
        self.wait(3)
        self.play(FadeOut(text1, math1, math2, math3))

        
class Proof(Scene):
    def construct(self):
        self.math_font_size = 40
        
        text1 = Tex("Proof",
                    color = WHITE,
                    font_size = self.math_font_size)

        text2 = Tex("Assuming $\\ln x$ is the inverse of $e^x$:",
                    color = WHITE,
                    font_size = self.math_font_size)

        math1 = MathTex(r'y &= \dfrac{dy}{dx}\\ y &= e^x \Longleftrightarrow \ln y = x',
                    color = WHITE,
                    font_size = self.math_font_size)

        math2 = MathTex(r'\dfrac{dy}{dx} &= y\\ \int\dfrac{1}{y}dy &= \int dx\\ &= x + C_0\\ &= \ln y + C_0',
                    color = WHITE,
                    font_size = self.math_font_size)

        text3 = Tex("Where $C_0 = 1$, given $(x_0, y_0) = (0, 1)$.",
                    color = WHITE,
                    font_size = self.math_font_size)

        
        math3 = Tex("$\\Box$",
                    color = WHITE,
                    font_size = self.math_font_size)
        
        VGroup(text1, text2, math1, math2, text3, math3).arrange(DOWN, aligned_edge = LEFT)
    
        self.play(Write(text1), runtime = 5)
        self.play(Write(text2), runtime = 5)
        self.play(Write(math1), runtime = 5)
        self.play(Write(math2), runtime = 5)
        self.play(Write(text3), runtime = 5)
        self.play(Write(math3), runtime = 5)
        self.wait(3)
        self.play(FadeOut(text1, text2, math1, math2, text3, math3))

