var SequenceSum = (function() {
  function SequenceSum() {}

  SequenceSum.showSequence = function(count) {
    let arr = []
    let res = 0
    for (let x = 0; x <= count; x++){
      res += x
      arr.push(x)
    }
    
    if (count < 0){
      return count + "<0"
    } else if (count === 0){
      return "0=0"
    } else {
      return arr.join("+") + " = " + res
    }
  };

  return SequenceSum;

})();
