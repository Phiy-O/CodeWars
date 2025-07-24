// [ 7 kyu ] Calculate mean and concatenate string
function mean(lst){
  let arrNum = []
  let arrStr = []
  let result = 0
  
  for (let x of lst){
    if ('1234567890'.includes(x)){
      arrNum.push(parseInt(x))
    } else {
      arrStr.push(x)
    }
  }
  
  for (let y of arrNum) {
    result += y
  }
  
  return [result / arrNum.length, arrStr.join('')];
}
