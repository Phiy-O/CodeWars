function isPowerOfTwo(n){
  //.. should return true or false ..
  if (n <= 0){
    return false
  } else if (n === 1 || n === 2){
    return true
  } else {
    while (n > 1){
      n = n / 2
    }
    return n === 1
  }
}
