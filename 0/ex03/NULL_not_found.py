def NULL_not_found(object: any) -> int:
  if type(object).__name__ == "NoneType":
    print(f"Nothing: None {type(object)}")
  elif type(object).__name__ == "float":
    print(f"Cheese: nan {type(object)}")
  elif type(object).__name__ == "int":
    if object == 0:
      print(f"Zero: 0 {type(object)}")
    else:
      print(f"Number: {type(object)}")
  elif type(object).__name__ == "bool":
    print(f"Fake: False {type(object)}")
  elif type(object).__name__ == "str" and len(object) == 0 :
    print(f"Empty: {type(object)}")
  else:
    print(f"Type not Found")
    return 1
  return 0
