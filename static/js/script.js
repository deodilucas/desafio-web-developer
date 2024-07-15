$(document).ready(function () {
    $('#data').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/pt-BR.json',
        },

        "ordering": true,
        columnDefs: [{
            orderable: false,
            targets: "no-sort"
        }]
    });
});

function clearInput () {
    document.getElementById('actionType').value = ''
    document.getElementById('dateExpected').value = ''
    document.getElementById('investmentExpected').value = ''
}