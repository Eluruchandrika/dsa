def tower_of_honoi(n,from_rod,to_rod,aux_rod):
  if n==0:
    return
  tower_of_honoi(n-1,from_rod,aux_rod,to_rod)
  print(f"move disk {n} from rod {from_rod} to {to_rod}")
  tower_of_honoi(n-1,aux_rod,to_rod,aux_rod)
  
n=3
tower_of_honoi(n,'a','b','c')