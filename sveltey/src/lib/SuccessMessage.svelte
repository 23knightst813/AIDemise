<script>
    export let show = false;
</script>

{#if show}
    <div class="success-message">Submitted </div>
{/if}

<style>
    .success-message {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
</style>