function Login() {
  const [code, setCode] = useState('');

  const handleInputChange = (event) => {
    setCode(event.target.value);
  };

  const handleQRCodeRead = () => {
    // Implementar funcionalidade de leitura de QR Code
    console.log('Ler QR Code');
  };

  return (
    <div className="qr-code-reader">
      <input
        type="text"
        value={code}
        onChange={handleInputChange}
        placeholder="Insira o código"
      />
      <button onClick={handleQRCodeRead}>Ler QR Code</button>
    </div>
  );
}
export default Control;
