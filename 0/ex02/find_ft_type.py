def all_thing_is_obj(object: any) -> int:
  if type(object).__name__ == "str":
    print(f"{object} is in the kitchen: {type(object)}")
  elif type(object).__name__ == "int":
    print(f"Type not Found")
  else:
    print(f"{type(object).__name__}: {type(object)}")
  return 42
