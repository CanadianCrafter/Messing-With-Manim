from manim import *
#Run: manim -pqh ParametricHeart.py ParametricHeart
class ParametricHeart(ThreeDScene):
    def write_message(self, message, run_time):
        self.play(Write(message, run_time = run_time))
        self.wait(2)
        self.play(Unwrite(message, reversed=True), run_time=1)
        self.wait(1)
    def construct(self):
        self.camera.background_color="#fae8f3"
        colors = ["#b51414"]
        surface = ParametricFunction(
            lambda u: np.array([
                (1/6) * np.sin(2*u)*(1 + np.cos(80*u)) * (1-(1/12)*((np.sin(2*u))**8)),
                (-1/2)*((2*u/PI-1)**2) + (1/7)*np.sin(2*u)*((np.sin(80*u))**3),
                0
            ]), t_range=[0,PI]
        ).scale(10)
        surface.set_color_by_gradient(colors)
        self.play(Create(surface, stroke_width = 0.1), run_time = 20)
        self.wait(5)



