class Recipe:
    def __init__(
        self, 
        id, 
        title, 
        ingredients, 
        instructions, 
        tags=None,
        image=None
    ):
        self.id = id
        self.title = title
        self.ingredients = ingredients  # list of ingredient dictionaries, e.g. [{"name": "rice", "quantity": "2 cups"}]
        self.instructions = instructions
        self.tags = tags if tags is not None else set()
        self.image = image

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)

    @classmethod
    def load_from_json(cls, recipe_json):
        recipe = cls(
            id=recipe_json["id"],
            title=recipe_json["title"],
            ingredients=recipe_json["ingredients"],
            instructions=recipe_json["instructions"],
            tags=set(recipe_json["tags"]),
            image=recipe_json.get("image", None)
        )
        return recipe

    def __str__(self):
        return f"Recipe: {self.title}, ID: {self.id}, Tags: {', '.join(self.tags)}"

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.id}')"