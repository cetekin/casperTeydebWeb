function pass_func(template_values) {
        $(document).ready(function() {
                /* Getting the opinion mining results */
                var aspectStats = JSON.parse(template_values["aspectStats"]);
                var aspectList = [];
                var positiveCntList = [];
                var negativeCntList = [];

                /* Extracting info from dict */
                for (var aspect in aspectStats) {
                        aspectList.push(aspect);
                        positiveCntList.push(parseInt(aspectStats[aspect]["positiveCnt"]));
                        negativeCntList.push(parseInt(aspectStats[aspect]["negativeCnt"])*-1);

                }
                /* Declaring bar stacked bar chart variable */
                var ctx = document.getElementById('aspectStatsChart');

                var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: {
                                labels: aspectList,
                                datasets: [{
                                                label: 'Pozitif Yorum Sayısı',
                                                data: positiveCntList,
                                                backgroundColor: '#D6E9C6' // green
                                        },
                                        {
                                                label: 'Negatif Yorum Sayısı',
                                                data: negativeCntList,
                                                backgroundColor: '#EBCCD1' // red
                                        }
                                ]
                        },
                        options: {
                                scales: {
                                        xAxes: [{
                                                stacked: true
                                        }],
                                        yAxes: [{
                                                stacked: true
                                        }]
                                }
                        }
                });

                $( "#dismiss-button" ).before("Yukarıdaki çubuk grafik; "+template_values["textCount"]+ " adet değerlendirme metni üzerinde analiz yapılarak, " + template_values["reportDate"] + " tarihinde oluşturulmuştur.");

        });

}
