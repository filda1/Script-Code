
<h2>Listado de Posts</h2>

<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Contenido</th>
            <th colspan="2"></th>
        </tr>
    </thead>
    <tbody>
        @foreach ($posts as $post)
        <tr>
            <td>{{ $post->id }}</td>
            <td>{{ $post->title }}</td>
            <td>{{ $post->body }}</td>
            <td>
                <button wire:click="edit({{ $post->id }})" class="btn btn-outline-primary">
                    Editar
                </button>
            </td>
            <td>
                <button wire:click="destroy({{ $post->id }})" class="btn btn-outline-danger">
                    Eliminar
                </button>
            </td>
        </tr>
        @endforeach
    </tbody>
</table>

{{ $posts->links() }}
