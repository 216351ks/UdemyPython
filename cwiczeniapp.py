class Direction:
    DOWN  = +1,  0
    UP    = -1,  0
    RIGHT =  0, +1
    LEFT  =  0, -1

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        self.end = None
    def terminate(self, end):
        self.end = end
    def terminated(self):
        return self.end is not None
    def distance(self, target):
        origin_row, origin_col = self.origin
        target_row, target_col = target
        delta_row, delta_col = target_row-origin_row, target_col-origin_col
        dir_row, dir_col = self.direction
        def decide(perp_delta, par_delta, dir_sign):
            if perp_delta or par_delta*dir_sign < 0:
                return None
            return abs(par_delta)
        return (decide(delta_row, delta_col, dir_col) if dir_row == 0 else 
                decide(delta_col, delta_row, dir_row) if dir_col == 0 else None)

class Entity:
    def __init__(self, space, location, direction):
        self.space = space
        self.location = location
        self.direction = direction
    def fire(self):
        pass
    def hit(self, ray):
        pass

class Enemy(Entity):
    def __init__(self, symbol, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = symbol
        self.destroyed = False
    def hit(self, ray):
        self.destroyed = True

class Mirror(Entity):
    def hit(self, ray):
        ray.terminate(self.location)
        mirror_row, mirror_col = self.direction
        sign = mirror_row or mirror_col
        ray_row, ray_col = ray.direction
        new_ray = Ray(self.location, (sign*ray_col, sign*ray_row))
        self.space.add_ray(new_ray)

class Ship(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mirrors = [Mirror(self.space, self.location, Direction.UP),
                        Mirror(self.space, self.location, Direction.DOWN)]
    def fire(self):
        self.space.add_ray(Ray(self.location, self.direction))
    def hit(self, ray):
        ray.terminate(self.location)
        ray_row, ray_col = ray.direction
        dir_row, dir_col = self.direction
        if ray_row == -dir_row and ray_col == -dir_col:
            for mirror in self.mirrors:
                mirror.hit(ray)

class Space:
    def __init__(self):
        self.entities = []
        self.rays = []
    def add_entity(self, entity):
        self.entities.append(entity)
    def add_ray(self, ray):
        self.rays.append(ray)
    def trace(self, ray):
        candidates = ((ray.distance(ent.location), ent) for ent in self.entities)
        targets = sorted((d, ent) for d, ent in candidates if d)
        for _, target in targets:
            if ray.terminated():
                break
            target.hit(ray)
    def fire_and_trace(self):
        for ent in self.entities:
            ent.fire()
        while self.rays:
            self.trace(self.rays.pop())

def parse(battlefield):
    space = Space()
    ships = {'>': Direction.RIGHT, '<': Direction.LEFT, '^': Direction.UP, 'v': Direction.DOWN}
    mirrors = {'/': Direction.UP, '\\': Direction.DOWN}
    for r, row in enumerate(battlefield):
        for c, char in enumerate(row):
            kwargs = dict(space=space, location=(r, c), direction=None)
            cls = None
            if char.isupper():
                kwargs.update(symbol=char)
                cls = Enemy
            elif char in ships:
                kwargs.update(direction=ships[char])
                cls = Ship
            elif char in mirrors:
                kwargs.update(direction=mirrors[char])
                cls = Mirror
            if cls:
                space.add_entity(cls(**kwargs))
    return space

def laser(battlefield):
    space = parse(battlefield)
    space.fire_and_trace()
    destroyed = (enemy.symbol for enemy in space.entities
                 if isinstance(enemy, Enemy) and enemy.destroyed)
    return sorted(destroyed),