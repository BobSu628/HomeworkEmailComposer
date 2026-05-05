def generate_email(row):
    return f"""
    <h2>Hello {row.get('name')}</h2>
    <p>Your weekly task:</p>
    <strong>{row.get('task')}</strong>
    """