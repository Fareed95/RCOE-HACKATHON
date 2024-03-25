
const options = {
  // add data series via arrays, learn more here: https://apexcharts.com/docs/series/
  series: [
    {
      name: "Developer Edition",
      data: [1500, 1418, 1456, 1526, 1356, 1256],
      color: "#1A56DB",
    },
    {
      name: "Designer Edition",
      data: [643, 413, 765, 412, 1423, 1731],
      color: "#7E3BF2",
    },
  ],
  chart: {
    height: "100%",
    maxWidth: "100%",
    type: "area",
    fontFamily: "Inter, sans-serif",
    dropShadow: {
      enabled: false,
    },
    toolbar: {
      show: false,
    },
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
  },
  legend: {
    show: true
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.55,
      opacityTo: 0,
      shade: "#1C64F2",
      gradientToColors: ["#1C64F2"],
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    width: 6,
  },
  grid: {
    show: false,
    strokeDashArray: 4,
    padding: {
      left: 2,
      right: 2,
      top: -26
    },
  },
  xaxis: {
    categories: ['01 February', '02 February', '03 February', '04 February', '05 February', '06 February', '07 February'],
    labels: {
      show: false,
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    show: false,
    labels: {
      formatter: function (value) {
        return '$' + value;
      }
    }
  },
  }
  
  if (document.getElementById("legend-chart") && typeof ApexCharts !== 'undefined') {
  const chart = new ApexCharts(document.getElementById("legend-chart"), options);
  chart.render();
  }
  

// sliders
    // var swiper = new Swiper(".mySwiper", {
    //   slidesPerView: 1,
    //   spaceBetween: 30,
    //   loop: true,
    //   pagination: {
    //     el: ".swiper-pagination",
    //     clickable: true,
    //   },
    //   navigation: {
    //     nextEl: ".swiper-button-next",
    //     prevEl: ".swiper-button-prev",
    //   },
    // });


    const getChartOptions = () => {
      return {
        series: [35.1, 23.5, 2.4, 5.4],
        colors: ["#1C64F2", "#16BDCA", "#FDBA8C", "#E74694"],
        chart: {
          height: 320,
          width: "100%",
          type: "donut",
        },
        stroke: {
          colors: ["transparent"],
          lineCap: "",
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                name: {
                  show: true,
                  fontFamily: "Inter, sans-serif",
                  offsetY: 20,
                },
                total: {
                  showAlways: true,
                  show: true,
                  label: "Unique visitors",
                  fontFamily: "Inter, sans-serif",
                  formatter: function (w) {
                    const sum = w.globals.seriesTotals.reduce((a, b) => {
                      return a + b
                    }, 0)
                    return '$' + sum + 'k'
                  },
                },
                value: {
                  show: true,
                  fontFamily: "Inter, sans-serif",
                  offsetY: -20,
                  formatter: function (value) {
                    return value + "k"
                  },
                },
              },
              size: "80%",
            },
          },
        },
        grid: {
          padding: {
            top: -2,
          },
        },
        labels: ["Direct", "Sponsor", "Affiliate", "Email marketing"],
        dataLabels: {
          enabled: false,
        },
        legend: {
          position: "bottom",
          fontFamily: "Inter, sans-serif",
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return value + "k"
            },
          },
        },
        xaxis: {
          labels: {
            formatter: function (value) {
              return value  + "k"
            },
          },
          axisTicks: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
        },
      }
    }
    
    if (document.getElementById("donut-chart") && typeof ApexCharts !== 'undefined') {
      const chart = new ApexCharts(document.getElementById("donut-chart"), getChartOptions());
      chart.render();
    
      // Get all the checkboxes by their class name
      const checkboxes = document.querySelectorAll('#devices input[type="checkbox"]');
    
      // Function to handle the checkbox change event
      function handleCheckboxChange(event, chart) {
          const checkbox = event.target;
          if (checkbox.checked) {
              switch(checkbox.value) {
                case 'desktop':
                  chart.updateSeries([15.1, 22.5, 4.4, 8.4]);
                  break;
                case 'tablet':
                  chart.updateSeries([25.1, 26.5, 1.4, 3.4]);
                  break;
                case 'mobile':
                  chart.updateSeries([45.1, 27.5, 8.4, 2.4]);
                  break;
                default:
                  chart.updateSeries([55.1, 28.5, 1.4, 5.4]);
              }
    
          } else {
              chart.updateSeries([35.1, 23.5, 2.4, 5.4]);
          }
      }
    
      // Attach the event listener to each checkbox
      checkboxes.forEach((checkbox) => {
          checkbox.addEventListener('change', (event) => handleCheckboxChange(event, chart));
      });
    }

    

    

