function consonantCount(str) {
  // ...
  let count = 0
  for (let x of str.toLowerCase()){
    if ('bcdfghjklmnpqrstvwxyz'.includes(x)){
      count++
    }
  }
  return count
}
