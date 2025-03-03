import Swal from 'sweetalert2';

export async function showConfirmationDelete() {
    const result = await Swal.fire({
        icon: 'warning',
        html: `
            <h4 class="text-lg font-semibold">Apakah Anda yakin untuk menghapus produk ini dari transaksi pembelian?</h4>
        `,
        showCancelButton: true,
        confirmButtonColor: '#36c1e7',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!',
        reverseButtons: true,
        // buttonsStyling: false,
        allowOutsideClick: false
    })

    return result.isConfirmed;
}
