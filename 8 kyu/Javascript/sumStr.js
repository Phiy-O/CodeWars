const result = parseInt(a) + parseInt(b);
    if (a == "" && b == "") {
        return "0";
    }
    if (a == "") {
        return b;
    } else if (b == "") {
        return a;
    }
    return String(result);
}
