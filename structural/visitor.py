from abc import ABC, abstractmethod


class AbstractCoordHolder(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class BBoxHolder(AbstractCoordHolder):

    def __init__(self, bbox_coords):
        for coord in bbox_coords:
            x1, y1, x2, y2 = coord
            assert (x1 < x2) & (y1 < y2)
        self.coords = bbox_coords

    def accept(self, visitor):
        visitor.visit(self)


class KeypointHolder(AbstractCoordHolder):

    def __init__(self, keypoint_coords):
        for coords in keypoint_coords:
            assert len(coords) == len(keypoint_coords[0])
        self.coord = keypoint_coords

    def accept(self, visitor):
        visitor.visit(self)


class AbstractVisitor(ABC):

    def visit(self, coord_holder):
        if isinstance(coord_holder, BBoxHolder):
            self.visit_bbox_holder(coord_holder)
        elif isinstance(coord_holder, KeypointHolder):
            self.visit_keypoint_holder(coord_holder)

    @abstractmethod
    def visit_bbox_holder(self, bbox_holder):
        pass

    @abstractmethod
    def visit_keypoint_holder(self, keypoint_holder):
        pass


class CvtBbox(AbstractVisitor):

    def visit_bbox_holder(self, bbox_holder):
        xywh = []
        for coord in bbox_holder.coords:
            x1, y1, x2, y2 = coord
            x = (x1 + x2) // 2
            y = (y1 + y2) // 2
            w = x2 - x1
            h = y2 - y1
            xywh.append([x, y, w, h])
        return xywh

    def visit_keypoint_holder(self, keypoint_holder):
        