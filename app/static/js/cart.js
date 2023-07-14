function addToSum(num) {
    var sumElement = document.getElementById("sum");
    var currentSum = parseInt(sumElement.innerHTML);
    var newSum = currentSum + num;
    sumElement.innerHTML = newSum;
  }

  function subtractFromSum(num) {
    var sumElement = document.getElementById("sum");
    var currentSum = parseInt(sumElement.innerHTML);

    if (currentSum > 0) {
      var newSum = currentSum - num;
      sumElement.innerHTML = newSum;
    }
  }