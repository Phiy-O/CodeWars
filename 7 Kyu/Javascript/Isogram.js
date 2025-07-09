function isIsogram(str){
  let obj = []
  for (let x of str.toLowerCase()){
    if (obj.includes(x)){
      return false
    }
    obj.push(x)
  }
  return true
}
