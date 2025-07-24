function squareRoot(x) {
  //Good luck!
  let sqrt = x ** (1/2)
  if (sqrt.toString().length === 1) {
    return sqrt
  } else {
    return parseFloat(sqrt.toFixed(5))
  }
}
