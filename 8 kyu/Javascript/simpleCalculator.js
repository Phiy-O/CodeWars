function calculator(a,b,sign){
    a = parseInt(a)
    b = parseInt(b)
    
    if (sign == "+") {
        if (a !== parseInt(a) || b !== parseInt(b)) {
            return "unknown value";
        } else {
            return a + b;
        }
    } else if (sign == "-") {
        if (a !== parseInt(a) || b !== parseInt(b)) {
            return "unknown value";
        } else {
            return a - b;
        } 
    } else if (sign == "*") {
        if (a !== parseInt(a) || b !== parseInt(b)) {
            return "unknown value";
        } else {
            return a * b;
        }
    } else if (sign == "/") {
        if (a !== parseInt(a) || b !== parseInt(b)) {
            return "unknown value";
        } else {
            return a / b;
        }
    } else {
      return "unknown value";
    }
}
