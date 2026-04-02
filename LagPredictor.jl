open System
open System.Security.Cryptography
open System.Text

type Transaction = {
    Id: Guid
    Player: string
    Amount: decimal
    Timestamp: DateTime
}

module SecurityKernel =
    let generateSecureHash (input: string) =
        use sha256 = SHA256.Create()
        input 
        |> Encoding.UTF8.GetBytes 
        |> sha256.ComputeHash 
        |> Convert.ToHexString

    let validateTransaction (tx: Transaction) =
        printfn "[F# KERNEL] Validating transaction %A for player %s" tx.Id tx.Player
        if tx.Amount < 0m then 
            Error "Negative transaction blocked!"
        else 
            let hash = generateSecureHash (tx.Player + tx.Amount.ToString())
            Ok (sprintf "SECURE_SIG_%s" hash)

[<EntryPoint>]
let main argv =
    let myTx = { Id = Guid.NewGuid(); Player = "Gracz1"; Amount = 49.99m; Timestamp = DateTime.Now }
    match SecurityKernel.validateTransaction myTx with
    | Ok sigStr -> printfn "[SUCCESS] Signature generated: %s" sigStr
    | Error msg -> printfn "[CRITICAL] %s" msg
    0