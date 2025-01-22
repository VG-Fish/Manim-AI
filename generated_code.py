from manim import *

class CoolManimAnimation(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN)

        circle.shift(LEFT*2)
        square.next_to(circle, RIGHT, buff=1)
        triangle.next_to(square, RIGHT, buff=1)


        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)

        self.play(circle.animate.scale(2), square.animate.rotate(PI/2), triangle.animate.shift(UP*2))
        self.wait(1)

        self.play(Transform(circle, square))
        self.wait(1)

        self.play(FadeOut(circle), FadeOut(square), FadeOut(triangle))

        text = Text("Cool Animation!", font_size=60)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))


        #Adding some extra flair
        dot = Dot(color=YELLOW)
        dot.shift(UP*2 + RIGHT*2)
        self.play(GrowFromCenter(dot))
        self.play(dot.animate.move_to(ORIGIN))
        self.play(ShrinkToCenter(dot))


        #Example of using a Path
        path = Line(start=ORIGIN, end=RIGHT*3)
        moving_dot = Dot(color=PURPLE)
        self.play(MoveAlongPath(moving_dot, path), run_time=3)
