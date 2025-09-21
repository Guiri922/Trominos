from manim import *

class Quads(Scene):
    def construct(self):

        square = Square(4,grid_xstep=2,grid_ystep=2,color=BLACK)
        b1 = Brace(square, LEFT, sharpness = 1, color = BLACK)
        t1 = MathTex('2^n', color=BLACK).next_to(b1, LEFT)
        p2 = [2,2,0]
        p1 = [2,0,0]
        b2 = BraceBetweenPoints(p1,p2,color=BLACK)
        t2 = MathTex('2^{n-1}',color=BLACK).next_to(b2, RIGHT)
        # tb = Text("B",color=BLACK).next_to(b2, 4*LEFT).scale(2)
        # ta = Text("A",color=BLACK).next_to(tb,5.5*LEFT).scale(2)
        # tc = Text("C",color=BLACK).next_to(ta,5.5*DOWN).scale(2)
        # td = Text("D",color=BLACK).next_to(tc, 5.5*RIGHT).scale(2)

        self.add(square, b1, t1, b2, t2)
        # self.add(ta,tb,tc,td)