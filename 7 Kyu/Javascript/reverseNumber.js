function reverseNumber(n) {
  let result = []
  for (let x of n.toString().split('').reverse()){
    if ('123456789'.includes(x)){
        result.push(x)
    }
  }

  if (n === 0) {
    return 0
  } else if (n < 0){
    return -result.join('')
  } else {
    return parseInt(result.join(''))
  }
}
