import UIKit

class HexletGitViewController: UIViewController {
    
    // MARK: - UI Elements
    private let hexletLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Thank you, Hexlet!"
        label.textAlignment = .center
        return label
    }()
    
    // MARK: - View Life Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(hexletLabel)
        NSLayoutConstraints.activate([
            hexletLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            hexletLabel.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor),
        ])
    }
}
