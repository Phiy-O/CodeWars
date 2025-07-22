function filterString(value) {
  //Complete this function :)
  let arr = []
  for (let x of value){
    if ('1234567890'.includes(x)){
      arr.push(x)
    }
  }
  return parseInt(arr.join(""))
}
