from manim import (
    AnimationGroup,
    Circle,
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    Line,
    ManimColor,
    Rectangle,
    ReplacementTransform,
    RoundedRectangle,
    Scene,
    Text,
    Transform,
    VGroup,
)


FONT = "Apple SD Gothic Neo"
BACKGROUND = ManimColor("#070A12")
PRIMARY = ManimColor("#F5F7FF")
CURRENT_ACCENT = ManimColor("#58D6C7")
NEXT_ACCENT = ManimColor("#FFD166")
MUTED = ManimColor("#AEB8CC")


def input_token(digit: str, color: ManimColor) -> VGroup:
    border = Circle(radius=0.38, color=color, stroke_width=5)
    label = Text(digit, font=FONT, font_size=52, color=PRIMARY)
    return VGroup(border, label)


class HalfAdderScene1(Scene):
    """Episode 001, scene 1: visually derive 1 + 1 = 10₂."""

    def construct(self) -> None:
        self.camera.background_color = BACKGROUND

        title = Text(
            "1 + 1은 왜 10이 될까?",
            font=FONT,
            font_size=40,
            weight="BOLD",
            color=PRIMARY,
        ).move_to([0, 3.35, 0])
        title_rule = Line(
            [-1.75, 3.0, 0],
            [1.75, 3.0, 0],
            color=MUTED,
            stroke_width=2,
        )

        left_one = input_token("1", NEXT_ACCENT).move_to([-0.85, 2.05, 0])
        plus = Text("+", font=FONT, font_size=48, color=PRIMARY).move_to([0, 2.05, 0])
        right_one = input_token("1", CURRENT_ACCENT).move_to([0.85, 2.05, 0])

        one_place_box = RoundedRectangle(
            width=2.55,
            height=2.15,
            corner_radius=0.22,
            color=CURRENT_ACCENT,
            stroke_width=5,
        ).move_to([0, 0.35, 0])
        one_place_label = Text(
            "한 자리",
            font=FONT,
            font_size=32,
            color=PRIMARY,
        ).move_to([0, -0.35, 0])

        stacked_top = [0, 0.73, 0]
        stacked_bottom = [0, -0.03, 0]
        rule = Text(
            "한 자리에는  0  또는  1",
            font=FONT,
            font_size=32,
            color=PRIMARY,
        ).move_to([0, -1.55, 0])
        rule_border = RoundedRectangle(
            width=3.75,
            height=0.68,
            corner_radius=0.15,
            color=MUTED,
            stroke_width=2,
        ).move_to(rule)
        rule_group = VGroup(rule_border, rule)

        next_box = Rectangle(
            width=1.45,
            height=1.65,
            color=NEXT_ACCENT,
            stroke_width=5,
        ).move_to([-0.95, 0.35, 0])
        current_box_target = RoundedRectangle(
            width=1.45,
            height=1.65,
            corner_radius=0.22,
            color=CURRENT_ACCENT,
            stroke_width=5,
        ).move_to([0.95, 0.35, 0])

        next_digit = Text("1", font=FONT, font_size=72, color=PRIMARY).move_to(next_box)
        current_digit = Text("0", font=FONT, font_size=72, color=PRIMARY).move_to(
            current_box_target
        )
        next_label = Text(
            "다음 자리",
            font=FONT,
            font_size=28,
            color=NEXT_ACCENT,
        ).next_to(next_box, DOWN, buff=0.18)
        current_label = Text(
            "현재 자리",
            font=FONT,
            font_size=28,
            color=CURRENT_ACCENT,
        ).next_to(current_box_target, DOWN, buff=0.18)

        equation_prefix = Text(
            "1 + 1 =",
            font=FONT,
            font_size=42,
            color=PRIMARY,
        ).move_to([-0.72, -2.05, 0])
        binary_digits = Text(
            "10",
            font=FONT,
            font_size=68,
            weight="BOLD",
            color=PRIMARY,
        ).move_to([0.82, -2.0, 0])
        binary_subscript = Text(
            "2",
            font=FONT,
            font_size=28,
            color=MUTED,
        ).move_to([1.35, -2.28, 0])
        binary_number = VGroup(binary_digits, binary_subscript)

        binary_label = Text(
            "이진수",
            font=FONT,
            font_size=30,
            color=NEXT_ACCENT,
        ).move_to([0.98, -2.85, 0])
        binary_label_border = RoundedRectangle(
            width=1.55,
            height=0.58,
            corner_radius=0.14,
            color=NEXT_ACCENT,
            stroke_width=2,
        ).move_to(binary_label)
        binary_label_group = VGroup(binary_label_border, binary_label)

        # 0:00–0:00.8 — introduce the question.
        self.play(FadeIn(title), Create(title_rule), run_time=0.8)

        # 0:00.8–0:01.6 — show the two input ones and one digit position.
        self.play(
            FadeIn(left_one),
            FadeIn(plus),
            FadeIn(right_one),
            FadeIn(one_place_box),
            FadeIn(one_place_label),
            run_time=0.8,
        )

        # 0:01.6–0:02.8 — the two ones meet inside the same position.
        self.play(
            left_one.animate.move_to(stacked_top),
            right_one.animate.move_to(stacked_bottom),
            FadeOut(plus),
            FadeOut(one_place_label),
            run_time=1.2,
        )

        # 0:02.8–0:03.8 — state the one-bit constraint visually.
        self.play(
            FadeIn(rule_group),
            one_place_box.animate.set_stroke(width=7),
            run_time=1.0,
        )

        # 0:03.8–0:05.2 — split into the next position 1 and current position 0.
        self.play(
            Transform(one_place_box, current_box_target),
            Create(next_box),
            ReplacementTransform(left_one, next_digit),
            ReplacementTransform(right_one, current_digit),
            FadeOut(rule_group),
            run_time=1.4,
        )

        # 0:05.2–0:06.2 — identify the positions using words and border shapes.
        self.play(FadeIn(next_label), FadeIn(current_label), run_time=1.0)

        # 0:06.2–0:07.3 — introduce the equation while preserving both positions.
        self.play(FadeIn(equation_prefix), run_time=1.1)

        # 0:07.3–0:08.5 — complete 10₂ and reveal its binary-number label together.
        self.play(
            AnimationGroup(
                FadeIn(binary_number),
                FadeIn(binary_label_group),
                lag_ratio=0.0,
            ),
            run_time=1.2,
        )

        # 0:08.5–0:10 — fixed reading hold; no animation.
        self.wait(1.5)
