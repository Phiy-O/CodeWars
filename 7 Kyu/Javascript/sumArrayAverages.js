const sumAverage = (arr) => {
  let obj = []
  for (let x = 0; x < arr.length; x++){
    const sum = arr[x].reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    obj.push(sum / arr[x].length)
  }
  const finalSum = obj.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  return Math.floor(finalSum)
}
