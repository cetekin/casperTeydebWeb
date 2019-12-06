function resetCanvas() {
    $('#aspectStatsChart').remove();
    $('#canvas-cont').prepend('<canvas class="mt-5" id="aspectStatsChart"></canvas>');
};

function init_bar_graph(aspect_based) {

    var labels,data1,data2;
    var yuzde_or_sayi = "";

    /* Aspect-based graph */
    if (aspect_based) {
        labels = ab_preserved_labels;
        data1 = ab_preserved_data1;
        data2 = ab_preserved_data2;
        yuzde_or_sayi = " Sayısı";
    }
    /* General graph */
    else {
        labels = general_preserved_labels;
        data1 = general_preserved_data1;
        data2 = general_preserved_data2;
        yuzde_or_sayi = " Yüzdesi";
    }

    resetCanvas();

    var ctx = document.getElementById('aspectStatsChart');

    var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                    labels: labels,
                    datasets: [{
                                    label: 'Pozitif Yorum'+yuzde_or_sayi,
                                    data: data1,
                                    backgroundColor: '#D6E9C6' // green
                            },
                            {
                                    label: 'Negatif Yorum'+yuzde_or_sayi,
                                    data: data2,
                                    backgroundColor: '#EBCCD1' // red
                            }
                    ]
            },
            options: {
                    scales: {
                            xAxes: [{
                                    stacked: aspect_based
                            }],
                            yAxes: [{
                                    stacked: aspect_based
                            }]
                    }
            }
    });


}

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

                /* Preserving the report datas for general and aspect-based graphs seperately */
                ab_preserved_labels = aspectList;
                ab_preserved_data1 = positiveCntList;
                ab_preserved_data2 = negativeCntList;
                general_preserved_labels = ["Yorumlar"]
                general_preserved_data1 = [template_values["generalStats"]["positiveTotalCnt"]]
                general_preserved_data2 = [template_values["generalStats"]["negativeTotalCnt"]]

                init_bar_graph(true);


                for (var i = 0; i < template_values["deviceList"].length; i++) {
                        $("#device_list").append("<option value='"+template_values["deviceList"][i]+"'>"+template_values["deviceList"][i]+"</option>");
                }
                $("#device_list").val(template_values["deviceName"]).change();


                $( "#dismiss-button" ).before("Yukarıdaki çubuk grafik; "+template_values["textCount"]+ " adet değerlendirme metni üzerinde analiz yapılarak, " + template_values["reportDate"] + " tarihinde oluşturulmuştur.");

                $('input[type=radio][name=inlineDefaultRadiosExample]').change(function() {

                    if (this.value == 'aspect-based') {
                        init_bar_graph(true);
                    } else if (this.value == 'general') {
                        init_bar_graph(false);
                    }
                });

        });

}
