class Solution:
    def on_segment(self, p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0 
        return 1 if val > 0 else 2 

    def doIntersect(self, p1, q1, p2, q2):
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        if (o1!= o2 and o3!= o4):
            return True

        if (o1 == 0 and self.on_segment(p1, p2, q1)):
            return True

        if (o2 == 0 and self.on_segment(p1, q2, q1)):
            return True

        if (o3 == 0 and self.on_segment(p2, p1, q2)):
            return True

        if (o4 == 0 and self.on_segment(p2, q1, q2)):
            return True

        return "false"
