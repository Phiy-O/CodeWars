function bingo(a) {
  // your winning code here
  // BINGO -> 2 9 14 7 15
  let bingoNumber = [2, 9, 14, 7, 15]
  let result = []
  for (let x of a){
    if (bingoNumber.includes(x) && !(result.includes(x))){
      result.push(x)
    }
  }
  
  if (result.length === bingoNumber.length) {
    return "WIN"
  }
  return "LOSE"
}
