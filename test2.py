def main():

  score = []

  # Enter 10 scores
  for i in range(10):
    score.append(float(input(f"Enter scores {i + 1}: ")))

  # Highest - lowest score
  high = max(score)
  low = min(score)
  print(f"Highest score: {high}")
  print(f"Lowest score: {low}")

  # Average
  average = sum(score) / len(score)
  print(f"Average: {average}")

  # Second score
  second = sorted(score, reverse=True)[1]
  print(f"Second largest score: {second}")

  # Check greater than 100
  check = any(diem > 100 for diem in score)
  if check:
    print("A value over 100 has been entered!")

  # Drop two lowest - Average the rest
  score.remove(low)
  score.remove(sorted(score)[0]) 
  average_rest = sum(score) / len(score)
  print(f"Average of the rest: {average_rest}")

if __name__ == "__main__":
  main()
