from dataclasses import dataclass


@dataclass(slots=True)
class Rect:
    x: int
    y: int
    width: int
    height: int

    def to_dict(self) -> dict[str, int]:
        return {'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height}

    def is_overlap_with_circle(self, px: int, py: int, r: int) -> bool:
        x_in_range: bool = self.x <= px <= self.x + self.width
        y_in_range: bool = self.y <= py <= self.y + self.height

        if x_in_range and y_in_range:
            return True
        elif x_in_range:
            return min(abs(py - self.y), abs(py - (self.y + self.height))) <= r
        elif y_in_range:
            return min(abs(px - self.x), abs(px - (self.x + self.width))) <= r
        else:
            xl: int = min(abs(px - self.x), abs(px - (self.x + self.width)))
            yl: int = min(abs(py - self.y), abs(py - (self.y + self.height)))
            return (xl * xl + yl * yl) <= (r * r)

    def get_overlap_len(self, other: 'Rect') -> float:
        # 计算两个矩形在x轴上的重叠长度
        # 如果x轴不重叠，返回负数
        x_overlap = min(self.x + self.width, other.x + other.width) - max(self.x, other.x)
        if x_overlap <= 0:
            return -1.0

        # 计算y轴上的重叠长度
        y_overlap = min(self.y + self.height, other.y + other.height) - max(self.y, other.y)
        if y_overlap <= 0:
            return -1.0

        # 返回重叠面积（或最小重叠维度）
        return float(min(x_overlap, y_overlap))
